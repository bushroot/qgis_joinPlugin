#
## https://gis.stackexchange.com/questions/31799/pyqgis-how-to-get-features-of-selected-geometries
#
#from qgis import core
#
##for layer in iface.legendInterface().layers():
##    print layer.name()
#    
#canvas = qgis.utils.iface.mapCanvas()
#cLayer = canvas.currentLayer()
#selectList = []
#
#selFeatures = cLayer.selectedFeatures
#
#for f in selFeatures:
#    print f.attributeMap()
#
#
#
#for f in features:
#    print f.attributeMap()
#
#if cLayer:
#    count = cLayer.selectedFeatureCount()
#    print count
#    selectedList = layer.selectedFeaturesIds()
#    for f in selectedList:
        # This is where I'm stuck
        # As I don't know how to get the Attributes of the features



###############
# https://nathanw.net/2011/02/23/total-length-of-selected-objects-qgis-via-python/
#layer = qgis.utils.iface.mapCanvas().currentLayer()
#for feature in layer:
#    print feature.name()
#i

# https://www.udemy.com/introduction-to-qgis-python-programming/learn/v4/t/lecture/6184202?start=0
from qgis import core

# List all layers
for layer in iface.legendInterface().layers():
    print layer.name()

# Get the selected layer
cLayer = qgis.utils.iface.mapCanvas().currentLayer()
print cLayer.name()

# Get selected features
for f in cLayer.selectedFeatures():
    print f["id_gs"]



# Know I should get only the selected feature





