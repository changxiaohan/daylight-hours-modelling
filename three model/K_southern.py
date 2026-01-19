import numpy as np
import math

# Data: latitude, sunrise, sunset
data = [
    (-34.925, "06:21", "20:31"),
    (-33.87, "06:03", "20:08"),
    (-3.107, "06:03", "18:19"),
    (-36.847, "06:22", "20:41"),
    (-12.092, "05:57", "18:41"),
    (-22.9, "06:24", "19:43"),
    (-21.133, "06:15", "19:28")
]

def time_to_hours(time_str):
    hours, minutes = time_str.split(':')
    return int(hours) + int(minutes)/60.0

# Calculate K for each location
latitudes_abs = []
K_values = []

t = 18  # January 19th

for lat, sunrise, sunset in data:
    daylight = time_to_hours(sunset) - time_to_hours(sunrise)
    sin_val = math.sin(2 * math.pi / 365 * (t - 264))
    K = (daylight - 12) / sin_val
    
    latitudes_abs.append(abs(lat))
    K_values.append(K)

# Cubic polynomial fitting
x = np.array(latitudes_abs)
y = np.array(K_values)
coeffs = np.polyfit(x, y, 3)

print(f"K = {coeffs[0]:.6f} * |lat|^3 + {coeffs[1]:.6f} * |lat|^2 + {coeffs[2]:.6f} * |lat| + {coeffs[3]:.6f}")