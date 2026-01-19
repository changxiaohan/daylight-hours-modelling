import math

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

print(daylight_southern(180, 90))