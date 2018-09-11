
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





