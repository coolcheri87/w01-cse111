# Cheri Hansen - cherilynne@byui.edu
# Created 5/3/2022
# CSE 111 - Christrian Elsinger
# Create a function to write, debug and understnad the program. '
# How to write your own functions.
# Import datetime so that it can be
# used to compute a person's age.

from datetime import datetime

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender=input("Please enter your gender F/M :  ")
    birth=input("Please enter your birthday in year, month, Day: ")
    height_inches=float(input("Please enter your height in inches: "))
    weight_lbs=float(input("Please enter your weight in pound:  "))
    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index, and basal_metabolic_rate functions
    # as needed.
    years=compute_age(birth)
    kg=kg_from_lb(weight_lbs)
    cm=cm_from_in(height_inches)
    mbi=body_mass_index(kg,cm)
    bmr=basal_metabolic_rate(gender, kg, cm, years)

    # Print the results for the user to see.
    print(f"Age (year): {years} years old.")
    print(f"Weight (Kg): {kg:.2f}. ")
    print(f"Height (cm): {cm:.2f}. ")
    print(f"Body mass index: {mbi:.2f}.")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}. ")

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg=pounds/2.205
    return kg


def cm_from_in(height_inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm=height_inches*2.54
    return cm


def body_mass_index(kg,cm):
    """Calculate and return a person's body mass index (bmi).
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi=10000*kg/cm**2
    return bmi


def basal_metabolic_rate(gender, kg, cm, years):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.upper() == "F":
        bmr=447.593+9.257*kg+3.098*cm-4.330*years
    else:
        bmr=88.362+13.397*kg+5.799*years
    return bmr


# Call the main function so that
# this program will start executing.

# Code that starts main()
main()
