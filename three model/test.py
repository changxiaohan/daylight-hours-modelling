import math
import matplotlib.pyplot as plt

def daylight_southern(t, lat):
    """
    Calculate daylight hours for the Southern Hemisphere.
    
    factors:
    t: int - Day time (jan 1st is t=0)
    lat: float - Latitude in degrees (negative for Southern Hemisphere)
    
    output:
    float - Daylight hours (clamped between 0 and 24)
    """
    # K value for Southern Hemisphere based on cubic polynomial fitting
    K = (0.000017 * abs(lat)**3 - 0.000446 * abs(lat)**2 + 0.061293 * abs(lat) + 0.114980)
    
    # Southern hemisphere formula with phase shift of 264 days (September 22nd equinox)
    daylight = 12 + K * math.sin(2 * math.pi / 365 * (t - 264))
    
    # Ensure daylight hours are within physical limits (0-24 hours)
    if daylight < 0:
        return 0
    elif daylight > 24:
        return 24
    else:
        return daylight

def daylight_northern(t, lat):
    """
    Calculate daylight hours for the Northern Hemisphere.
    
    factors:
    t: int - Day time (jan 1st is t=0)
    lat: float - Latitude in degrees (positive for Northern Hemisphere)
    
    output:
    float - Daylight hours (clamped between 0 and 24)
    """
    # K value for Northern Hemisphere based on cubic polynomial fitting
    K = -0.000006 * lat**3 + 0.001529 * lat**2 + 0.016594 * lat + 0.103280
    
    # Northern hemisphere formula with phase shift of 79 days (March 20th equinox)
    daylight = 12 + K * math.sin(2 * math.pi / 365 * (t - 79))
    
    # Ensure daylight hours are within physical limits (0-24 hours)
    if daylight < 0:
        return 0
    elif daylight > 24:
        return 24
    else:
        return daylight

def calculate_t(month, day):
    """
    Calculate t value from month and day.
    
    factors:
    month: int - Month (1-12)
    day: int - Day of month
    
    output:
    int - t value (0 for January 1st)
    """
    # Days in each month (non-leap year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Validate input
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    
    if day < 1 or day > month_days[month-1]:
        raise ValueError(f"Day must be between 1 and {month_days[month-1]} for month {month}")
    
    # Calculate t (0-based day of year)
    t = sum(month_days[:month-1]) + (day - 1)
    return t

def plot_yearly_daylight(lat, hemisphere_func):
    """
    Plot yearly daylight variation for a given latitude.
    
    factors:
    lat: float - Latitude in degrees
    hemisphere_func: function - Function to calculate daylight hours (northern or southern)
    """
    # Generate t values for the entire year
    days = list(range(365))
    daylight_hours = [hemisphere_func(t, lat) for t in days]
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(days, daylight_hours, 'b-', linewidth=2)
    plt.axhline(y=12, color='r', linestyle='--', alpha=0.5, label='12 hours (equinox reference)')
    
    # Add important dates
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

def interactive_daylight_calculator():
    """
    Interactive daylight hour calculator
    """
    print("=" * 60)
    print("DAYLIGHT HOUR CALCULATOR")
    print("=" * 60)
    print("Welcome! Please select your science level:")
    print("1. Science Rookie")
    print("2. Science Enthusiast")
    print("Enter 'q' to quit at any time")
    print("=" * 60)
    
    while True:
        # Get user type
        while True:
            user_type_str = input("\nEnter your science level (1(Science Rookie) or 2(Science Enthusiast)): ").strip()
            if user_type_str.lower() == 'q':
                print("Thank you for using the calculator!")
                return
            
            if user_type_str in ['1', '2']:
                user_type = int(user_type_str)
                break
            else:
                print("Error: Please enter '1' for Science Rookie or '2' for Science Enthusiast!")
        
        # Set user type description
        user_type_desc = "Science Rookie" if user_type == 1 else "Science Enthusiast"
        
        # Get latitude input
        while True:
            lat_str = input("Enter latitude (-90 to 90): ").strip()
            if lat_str.lower() == 'q':
                print("Thank you for using the calculator!")
                return
            
            try:
                lat = float(lat_str)
                if -90 <= lat <= 90:
                    break
                else:
                    print("Error: Latitude must be between -90 and 90!")
            except ValueError:
                print("Error: Please enter a valid number!")
        
        # Get month input
        while True:
            month_str = input("Enter month (1-12): ").strip()
            if month_str.lower() == 'q':
                print("Thank you for using the calculator!")
                return
            
            try:
                month = int(month_str)
                if 1 <= month <= 12:
                    break
                else:
                    print("Error: Month must be between 1 and 12!")
            except ValueError:
                print("Error: Please enter a valid integer!")
        
        # Get day input
        while True:
            day_str = input(f"Enter day (1-31, depends on month): ").strip()
            if day_str.lower() == 'q':
                print("Thank you for using the calculator!")
                return
            
            try:
                day = int(day_str)
                # Validate day based on month
                month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                max_day = month_days[month-1]
                
                if 1 <= day <= max_day:
                    break
                else:
                    print(f"Error: Day must be between 1 and {max_day} for month {month}!")
            except ValueError:
                print("Error: Please enter a valid integer!")
        
        try:
            # Calculate t value
            t = calculate_t(month, day)
            
            # Calculate daylight hours
            if lat < 0:
                # Southern Hemisphere
                hemisphere = "Southern Hemisphere"
                daylight = daylight_southern(t, lat)
                hemisphere_func = daylight_southern
            else:
                # Northern Hemisphere
                hemisphere = "Northern Hemisphere"
                daylight = daylight_northern(t, lat)
                hemisphere_func = daylight_northern
            
            # Display results
            print("\n" + "=" * 60)
            print(f"RESULTS FOR {user_type_desc}")
            print("=" * 60)
            print(f"Latitude: {lat}° ({hemisphere})")
            print(f"Date: Month {month}, Day {day}")
            print(f"Day of year (t value): {t+1}")
            print(f"Daylight hours: {daylight:.2f} hours")
            print("-" * 60)
            
            # Add explanation based on user type
            if user_type == 1:
                print("\nSCIENCE EXPLANATION FOR ROOKIES:")
                print("-" * 40)
                print("Imagine the Earth as a giant sphere, and the sun as a large lamp.")
                print("The Earth rotates once a day, which is why we have day and night.")
                print("However, the Earth doesn't rotate vertically; it's tilted, like your")
                print("head tilted to the side.\n")
                print("On Earth, different places are at varying distances from the North")
                print("and South Poles. Near the center (the equator), the sun shines for")
                print("roughly the same amount of time, so day and night are always roughly")
                print("the same length. But near the top or bottom (high latitudes), as the")
                print("Earth rotates to a certain position, the sun may shine for a very")
                print("long time, or it may not shine at all for a very long time.")
            else:
                print("\nSCIENCE EXPLANATION FOR ENTHUSIASTS:")
                print("-" * 40)
                print("The main reason for the variation in sunshine duration with latitude")
                print("is the approximately 23.5-degree tilt of the Earth's axis of rotation")
                print("relative to its orbital plane (i.e., the obliquity of the ecliptic),")
                print("and the Earth's revolution around the sun. As the Earth revolves")
                print("around the sun, the direction of its axis of rotation remains")
                print("constant, causing the point where the sun's rays are directly")
                print("overhead to shift between the Tropic of Cancer and the Tropic of")
                print("Capricorn (23.5°N to 23.5°S), thus resulting in seasonal variations")
                print("in sunshine duration at different latitudes.")
                
                # Plot yearly variation for Science Enthusiasts
                print("\n" + "-" * 40)
                print("GENERATING YEARLY DAYLIGHT VARIATION PLOT...")
                try:
                    plot_yearly_daylight(lat, hemisphere_func)
                except Exception as e:
                    print(f"Could not generate plot. Error: {e}")
                    print("Please make sure matplotlib is installed: pip install matplotlib")
            
            print("=" * 60)
            
        except ValueError as e:
            print(f"Error: {e}")

# Run interactive calculator
if __name__ == "__main__":
    interactive_daylight_calculator()