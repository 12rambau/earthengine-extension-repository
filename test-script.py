import ee
from vscee import Map

# Initialize the Earth Engine library
ee.Initialize(project="ldc-crop-monitor")

# Load the DMSP-OLS Nighttime Lights image collection and select the 'stable_lights' band
dataset = ee.ImageCollection('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS')
night_lights = dataset.select('stable_lights')

# Set the map center and add the night lights layer
Map.setCenter(30, 45, 3)
Map.addLayer(night_lights, {'min': 0, 'max': 63}, 'Nighttime Lights')
