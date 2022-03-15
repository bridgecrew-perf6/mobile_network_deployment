layer = QgsProject.instance().mapLayersByName('adm_edif_pub_civil_p')[0]

parameters = { 'INPUT' : layer, 
               'OUTPUT' : 'TEMPORARY_OUTPUT' }

processing.run('Mobile Network Deployment:generatehexagonareas', parameters)