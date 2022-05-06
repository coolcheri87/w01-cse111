def main():
    # Get an odometer value in U.S. miles from the user.
    odometer1 = float(input("Enter the first odometer reading (miles): "))

    # Get another odometer value in U.S. miles from the user.
    odometer2 = float(input("Enter the second odometer rading (miles): "))

    # Get a fuel amount in U.S. gallons from the user.
    fuel_amount = float(input("Enter amount of fuel used (gallons): "))

    # Call the miles_per_gallon function and store
    mpg = miles_per_gallon(odometer1, odometer2, fuel_amount)
    # the result in a variable named mpg.

    # Call the lp100k_from_mpg function to convert the
    lpk100k = lp100k_from_mpg(mpg)
    # miles per gallon to liters per 100 kilometers and
    
    # store the result in a variable named lp100k.

    # Display the results for the user to see.
    print(f"{mpg:,.1f} miles per gallon")
    print(f"{lpk100k:,.2f} liters per 100 kilometers")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg = (end_miles - start_miles)/ amount_gallons

    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k_from_mpg = 235.245/mpg

    return lp100k_from_mpg


# Call the main function so that
# this program will start executing.
main()