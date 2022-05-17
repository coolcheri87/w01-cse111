def wind_chill(temperature, wind_speed):
    """ Computer and return the wind chill factor as defined by the US National Weather SErvice.
    Parameters
        temperature: the air temperature in Fahrenheit at five feet 
            above the ground
        wind_speed: the spead of the wind in miles per hour at five feet above the ground
    return: the wind chill factor in degrees Fahrenheit.
    """
    chill_factor = 35.74 \
        + 0.6215 * temperature \
        - 35.75 * wind_speed**0.16 \
        + 0.4275 * temperature * wind_speed**0.16
    rounded = round(chill_factor, 1)
    return rounded


def heat_index(temperature, humidity):
    """Computer and reutrn the heat index as defined by the US National Weather SErvicel.
    
    Parmeters   
        temperature: the air temperature in Fairenheit at five feet above the ground.
        humidity: the relative humidity of the air at five feet above the ground
    Return: The heat index in degrees Fahrenteit.
    """

