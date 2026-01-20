# %%
#simple part(5.1 and 5.2)
import math
import matplotlib.pyplot as plt

def daylight(t, lat):
    K = 0.051*lat + 9.8 if lat >= 0 else \
        0.225*abs(lat) - 1.96
    phase = 79 if lat >= 0 else 264
    return max(0, min(24, 12 + K * math.sin(2 * math.pi / 365 * (t - phase))))

def calculate_t(month, day):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not 1 <= month <= 12: raise ValueError("Month must be between 1 and 12")
    if not 1 <= day <= month_days[month-1]: raise ValueError(f"Day must be between 1 and {month_days[month-1]} for month {month}")
    return sum(month_days[:month-1]) + day - 1

def plot_yearly_daylight(lat):
    days = list(range(365))
    daylight_hours = [daylight(t, lat) for t in days]
    
    plt.figure(figsize=(10, 6))
    plt.plot(days, daylight_hours, 'b-', linewidth=2)
    plt.axhline(y=12, color='r', linestyle='--', alpha=0.5, label='12 hours (equinox reference)')
    
    important_dates = [
        (79, 'Mar 20-21 (Spring Equinox)'),
        (172, 'Jun 21-22 (Summer Solstice)'),
        (265, 'Sep 22-23 (Autumn Equinox)'),
        (355, 'Dec 21-22 (Winter Solstice)')
    ]
    
    for t_date, label in important_dates:
        plt.axvline(x=t_date, color='gray', linestyle=':', alpha=0.7)
        plt.text(t_date, max(daylight_hours)*0.95, label, rotation=90, 
                verticalalignment='top', fontsize=8)
    
    plt.xlabel('Day of Year (t)', fontsize=12)
    plt.ylabel('Daylight Hours', fontsize=12)
    plt.title(f'Yearly Daylight Variation at Latitude {lat}°', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 365)
    plt.ylim(0, 24)
    plt.legend()
    plt.tight_layout()
    plt.show()

def get_input(prompt, type_func, valid_func=None, error_msg=None):
    while True:
        value = input(prompt).strip()
        if value.lower() == 'q': return None
        try:
            result = type_func(value)
            if not valid_func or valid_func(result): return result
            print(error_msg if error_msg else "Error: Invalid input!")
        except ValueError:
            print(error_msg if error_msg else "Error: Please enter a valid value!")

def interactive_daylight_calculator():
    print("DAYLIGHT HOUR CALCULATOR")
    print()
    print("Welcome! Please select your science level:")
    print("1. Science Rookie")
    print("2. Science Enthusiast")
    print("Enter 'q' to quit at any time")
    
    while True:
        print()
        user_type = get_input("Enter your science level (1 or 2): ", 
                             int, lambda x: x in [1, 2],
                             "Error: Please enter '1' for Science Rookie or '2' for Science Enthusiast!")
        if user_type is None: 
            print()
            print("Thank you for using the calculator!")
            return
        
        lat = get_input("Enter latitude (-90 to 90): ", 
                       float, lambda x: -90 <= x <= 90,
                       "Error: Latitude must be between -90 and 90!")
        if lat is None: 
            print()
            print("Thank you for using the calculator!")
            return
        
        month = get_input("Enter month (1-12): ", 
                         int, lambda x: 1 <= x <= 12,
                         "Error: Month must be between 1 and 12!")
        if month is None: 
            print()
            print("Thank you for using the calculator!")
            return
        
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        max_day = month_days[month-1]
        day = get_input(f"Enter day (1-{max_day}): ", 
                       int, lambda x: 1 <= x <= max_day,
                       f"Error: Day must be between 1 and {max_day} for month {month}!")
        if day is None: 
            print()
            print("Thank you for using the calculator!")
            return
        
        try:
            t = calculate_t(month, day)
            hrs = daylight(t, lat)
            hemisphere = "Northern Hemisphere" if lat >= 0 else "Southern Hemisphere"
            user_type_desc = "Science Rookie" if user_type == 1 else "Science Enthusiast"
            
            print()
            print(f"RESULTS FOR {user_type_desc}")
            print()
            print(f"Latitude: {lat}° ({hemisphere})")
            print(f"Date: Month {month}, Day {day}")
            print(f"Day of year (t value): {t+1}")
            print(f"Daylight hours: {hrs:.2f} hours")
            
            print()
            if user_type == 1:
                print("SCIENCE EXPLANATION FOR ROOKIES:")
                print()
                print("Imagine the Earth as a giant sphere, and the sun as a large lamp.")
                print("The Earth rotates once a day, which is why we have day and night.")
                print("However, the Earth doesn't rotate vertically; it's tilted, like your")
                print("head tilted to the side.")
                print()
                print("On Earth, different places are at varying distances from the North")
                print("and South Poles. Near the center (the equator), the sun shines for")
                print("roughly the same amount of time, so day and night are always roughly")
                print("the same length. But near the top or bottom (high latitudes), as the")
                print("Earth rotates to a certain position, the sun may shine for a very")
                print("long time, or it may not shine at all for a very long time.")
            else:
                print("SCIENCE EXPLANATION FOR ENTHUSIASTS:")
                print()
                print("The main reason for the variation in sunshine duration with latitude")
                print("is the approximately 23.5-degree tilt of the Earth's axis of rotation")
                print("relative to its orbital plane (i.e., the obliquity of the ecliptic),")
                print("and the Earth's revolution around the sun. As the Earth revolves")
                print("around the sun, the direction of its axis of rotation remains")
                print("constant, causing the point where the sun's rays are directly")
                print("overhead to shift between the Tropic of Cancer and the Tropic of")
                print("Capricorn (23.5°N to 23.5°S), thus resulting in seasonal variations")
                print("in sunshine duration at different latitudes.")
                
                print()
                print("GENERATING YEARLY DAYLIGHT VARIATION PLOT...")
                try:
                    plot_yearly_daylight(lat)
                except Exception as e:
                    print(f"Could not generate plot. Error: {e}")
                    print("Please make sure matplotlib is installed: pip install matplotlib")
            
            print()
            
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    interactive_daylight_calculator()

# %%
#advanced part(5.3)
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
    K = 0.051*lat + 9.8 if lat >= 0 else \
        0.225*abs(lat) - 1.96
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

print("Dear Science Enthusiast,My improved method performs less effectively than the advanced method at latitudes 45° and –45°, largely because the approach I used to determine parameter K is linear. Please note that the real-world data employed here are drawn from only two specific locations and therefore may not be fully representative of all geographic latitudes. Thus, actual daylight hours could differ from my estimates at certain points along the same latitude.Additionally, the performance of my method tends to degrade at higher latitudes. For example, at latitudes such as 90° or –90°, the improved method shows notably lower accuracy. For further enhancement, if you are interested, you could explore using a higher-order polynomial fit via numpy.polyfit to derive a better function for K in terms of latitude. Revising the parameter K in this way may help improve the method’s performance, particularly at high latitudes. Please feel free to reach out if you have any questions or would like to discuss further.")
# %%
