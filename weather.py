# test_weather.py
from decimal import Rounded
from weather import cels_from_fahr
from pytest import approx
import pytest

def test_cels_from_fahr():
    """Test the cels_from_fahr function by calling it and
    comparing the values it returns to the expected values.
    Notice this test function uses pytest.approx to compare
    floating point numbers.
    """
    assert cels_from_fahr(-25) == approx(-31.66667)
    assert cels_from_fahr(0) == approx(-17.77778)
    assert cels_from_fahr(32) == approx(0)
    assert cels_from_fahr(70) == approx(21.1111)

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

index = -42.379 \
    + 2.049045253 * temperature \
    + 10.1433127 * humidity \
    - 0.22475541 * temperature * humidity \
    - 0.00683783 * temperature**2 \
    - 0.05481717 * humidity**2 \
    + 0.00122874 * temperature**2 * humidity**2 
    rounded * round(index, 1)
    return rounded

def celx_from_fahr(fahr):
    """Convert a temperature in fahrenheit to 
    Celsius and return the Calisius temperature
    """
    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])