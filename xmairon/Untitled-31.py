def generate_site_radii(min, max, increment):
        for n in range(min, max, increment):
            yield n

INCREMENT_MA = (400, 30400, 2000) #(5000, 5500, 500) (400, 30400, 1000)
INCREMENT_MI = (25, 500, 25) #(40, 540, 80) (300, 400, 100)

SITE_RADII = {
    'macro': {
        'urban':
            generate_site_radii(INCREMENT_MA[0],INCREMENT_MA[1],INCREMENT_MA[2]),
        'suburban':
            generate_site_radii(INCREMENT_MA[0],INCREMENT_MA[1],INCREMENT_MA[2]),
        'rural':
            generate_site_radii(INCREMENT_MA[0],INCREMENT_MA[1],INCREMENT_MA[2])
        },
    'micro': {
        'urban':
            generate_site_radii(INCREMENT_MI[0],INCREMENT_MI[1],INCREMENT_MI[2]),
        'suburban':
            generate_site_radii(INCREMENT_MI[0],INCREMENT_MI[1],INCREMENT_MI[2]),
        'rural':
            generate_site_radii(INCREMENT_MI[0],INCREMENT_MI[1],INCREMENT_MI[2])
        },
    }

urban = generate_site_radii(INCREMENT_MA[0],INCREMENT_MA[1],INCREMENT_MA[2])
for item in urban:
    print(item)