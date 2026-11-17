import ee
from vscee import Map

# Initialize the Earth Engine library
ee.Initialize(project="earthengine-extension")

# Load the DMSP-OLS Nighttime Lights image collection and select the 'stable_lights' band
dataset = ee.ImageCollection('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS')

# Set the map center and add the night lights layer
Map.setCenter(30, 45, 3)
Map.addLayer(dataset, {'min': 0, 'max': 63}, 'Nighttime Lights')
