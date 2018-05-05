#!/usr/bin/python3
# height in inches
# weight in pounds
height = [76.77,  70.86,  72.83,  70.07,  75.98,  70.07,  70.01, 70.8]
weight = [209.439, 167.551, 182.984, 165.347, 216.053, 163.142, 176.37, 191.802]
# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m
# multiplication by  0.0254

np_height_m = np.array(height) * 0.0254 

# Create array from weight with correct units: np_weight_kg
# multiplication by 0.453592

np_weight_kg = np.array(weight) * 0.453592

# Calculate the BMI: bmi
# kg/m^2

bmi = np_weight_kg / np_height_m ** 2

# Print out bmi

print (bmi)
