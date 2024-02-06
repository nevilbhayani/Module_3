# Write a Python program to convert degree to radian.

import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

# Example usage:
degrees_value = 45

radians_value = degrees_to_radians(degrees_value)

print("Ans :",radians_value)
