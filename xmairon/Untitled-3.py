import math
import fiona
from shapely.ops import transform
from shapely.geometry import Point, mapping, shape, Polygon
from rtree import index

def calculate_polygons(startx, starty, endx, endy, radius):

    # calculate side length given radius
    sl = (2 * radius) * math.tan(math.pi / 6)

    # calculate coordinates of the hexagon points
    # sin(30)
    p = sl * 0.5
    b = sl * math.cos(math.radians(30))
    w = b * 2
    h = 2 * sl

    # offset start and end coordinates by hex widths and heights to guarantee
    # coverage
    startx = startx - w
    starty = starty - h
    endx = endx + w
    endy = endy + h

    origx = startx
    origy = starty

    # offsets for moving along and up rows
    xoffset = b
    yoffset = 3 * p

    polygons = []
    row = 1
    counter = 0

    while starty < endy:

        if row % 2 == 0:
            startx = origx + xoffset

        else:
            startx = origx

        while startx < endx:
            p1x = startx
            p1y = starty + p
            p2x = startx
            p2y = starty + (3 * p)
            p3x = startx + b
            p3y = starty + h
            p4x = startx + w
            p4y = starty + (3 * p)
            p5x = startx + w
            p5y = starty + p
            p6x = startx + b
            p6y = starty
            poly = [
                (p1x, p1y),
                (p2x, p2y),
                (p3x, p3y),
                (p4x, p4y),
                (p5x, p5y),
                (p6x, p6y),
                (p1x, p1y)]

            polygons.append(poly)

            counter += 1
            startx += w

        starty += yoffset
        row += 1

    return polygons



site_radius = 25
layer = QgsProject.instance().mapLayersByName('transmitter_25')[0]
test = QgsProject.instance().mapLayersByName('Buffered')[0]
pr = test.dataProvider()

for feature in layer.getFeatures():
    feature.geometry().asPoint()
    point = Point(feature.geometry().asPoint().x(),feature.geometry().asPoint().y())
    #print(point)
    geom_shape = shape(point)
    #print(geom_shape)
buffered = Polygon(geom_shape.buffer(site_radius*2).exterior)
pr.addFeature(buffered)

polygon = calculate_polygons(
    buffered.bounds[0], buffered.bounds[1],
    buffered.bounds[2], buffered.bounds[3],
    site_radius)
print(buffered.bounds[0])
for feat in test.getFeatures():
    a = feat.geometry().boundingBox()
    #print(a)