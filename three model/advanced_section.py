import numpy as np
import math
import matplotlib.pyplot as plt

def advanced_daylight(t, lat, axial_tilt_deg=23.44):
    phi_T = np.radians(axial_tilt_deg)
    
    if lat >= 0:
        phase = 79
        theta_L = np.radians(lat)
        inner_term = np.tan(theta_L) * np.tan(phi_T) * np.sin((2 * np.pi / 365) * (phase - t))
    else:
        phase = 264
        theta_L = np.radians(abs(lat))
        inner_term = np.tan(theta_L) * np.tan(phi_T) * np.sin((2 * np.pi / 365) * (t - phase))
    
    if inner_term > 1:
        inner_term = 1.0
    elif inner_term < -1:
        inner_term = -1.0
    
    if lat >= 0:
        daylight_hours = 12 + (24 / np.pi) * np.arcsin(-inner_term)
    else:
        daylight_hours = 12 + (24 / np.pi) * np.arcsin(inner_term)
    
    return max(0, min(24, daylight_hours))

def daylight(t, lat):
    K = -0.000006*lat**3 + 0.001529*lat**2 + 0.016594*lat + 0.103280 if lat >= 0 else \
        0.000017*abs(lat)**3 - 0.000446*abs(lat)**2 + 0.061293*abs(lat) + 0.114980
    phase = 79 if lat >= 0 else 264
    return max(0, min(24, 12 + K * math.sin(2 * math.pi / 365 * (t - phase))))

true_values_45 = {
    0: 8.8666,
    30: 9.83,
    60: 11.2,
    90: 12.7666,
    120: 14.2,
    150: 15.4,
    180: 15.6,
    210: 14.66,
    240: 13.2,
    270: 11.83,
    300: 10.66,
    330: 9.6,
    360: 9
}

true_values_n45 = {
    0: 15.5,
    30: 14.5,
    60: 13,
    90: 11.47,
    120: 10,
    150: 9,
    180: 8.82,
    210: 9.66,
    240: 11,
    270: 12.5,
    300: 14.2,
    330: 15.6,
    360: 15.5
}

t_full = np.linspace(0, 365, 366)

adv_45 = [advanced_daylight(t, 45) for t in t_full]
simple_45 = [daylight(t, 45) for t in t_full]

adv_n45 = [advanced_daylight(t, -45) for t in t_full]
simple_n45 = [daylight(t, -45) for t in t_full]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10), sharex=True)

ax1.plot(t_full, adv_45, 'b-', label='advanced_daylight', linewidth=2)
ax1.plot(t_full, simple_45, 'r-', label='daylight', linewidth=2)

t_points_45 = list(true_values_45.keys())
true_points_45 = list(true_values_45.values())
ax1.scatter(t_points_45, true_points_45, color='green', s=100, zorder=5, label='True Values', edgecolors='black')

ax1.set_ylabel('Daylight Hours', fontsize=12)
ax1.set_title('Latitude = 45° (Northern Hemisphere)', fontsize=14)
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 24)

ax2.plot(t_full, adv_n45, 'b-', label='advanced_daylight', linewidth=2)
ax2.plot(t_full, simple_n45, 'r-', label='daylight', linewidth=2)

t_points_n45 = list(true_values_n45.keys())
true_points_n45 = list(true_values_n45.values())
ax2.scatter(t_points_n45, true_points_n45, color='green', s=100, zorder=5, label='True Values', edgecolors='black')

ax2.set_xlabel('Day of Year (t)', fontsize=12)
ax2.set_ylabel('Daylight Hours', fontsize=12)
ax2.set_title('Latitude = -45° (Southern Hemisphere)', fontsize=14)
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)
ax2.set_ylim(0, 24)

plt.tight_layout()
plt.show()

print("Dear Science Enthusiast, Both my improved method and the advanced method perform effectively at latitudes 45° and -45°. However, please note that the real-world data used here come from two specific locations, and thus do not represent all geographic latitudes on Earth. Therefore, it remains possible that at certain locations along the same latitude, actual daylight hours may differ from the estimated values. Additionally, this does not imply that the improved method is equivalent to the advanced method in all scenarios. For instance, at latitudes such as 90° or -90°, the performance of the improved method is notably less accurate.For further enhancement, if you are interested, you could focus on improving the method's performance at high latitudes. Perhaps introducing a revised function for parameter K might yield better results in such cases.")