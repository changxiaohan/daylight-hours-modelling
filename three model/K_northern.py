import numpy as np
import math

# data: latitude, sunrise, sunset
northern_data = [
    (49.267, "07:59", "16:48"), 
    (19.4, "07:13", "18:22"),     
    (59.333, "08:24", "15:33"),
    (64.183, "08:24", "15:33"),   
    (6.442, "07:03", "18:51"),   
    (13.725, "06:46", "18:12")   
]

def time_to_hours(time_str):
    hours, minutes = time_str.split(':')
    return int(hours) + int(minutes)/60.0

# Calculate K for each location (Northern Hemisphere)
latitudes = []
K_values = []

t = 18  # January 19th

for lat, sunrise, sunset in northern_data:
    daylight = time_to_hours(sunset) - time_to_hours(sunrise)
    sin_val = math.sin(2 * math.pi / 365 * (t - 79)) 
    K = (daylight - 12) / sin_val
    
    latitudes.append(lat)
    K_values.append(K)

# Cubic polynomial fitting
x = np.array(latitudes)
y = np.array(K_values)
coeffs = np.polyfit(x, y, 3)

print(f"K = {coeffs[0]:.6f} * lat^3 + {coeffs[1]:.6f} * lat^2 + {coeffs[2]:.6f} * lat + {coeffs[3]:.6f}")
#K = (-0.000006 * lat**3 + 0.001529 * lat**2 + 0.016594 * lat + 0.103280)