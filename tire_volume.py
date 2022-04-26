# Cheri Hansen - cherilynne@byui.edu
# Created 4/21/2022
# Week 1 Assignment - CSE111-12
# Create a function that calculates volume from width, aspect ratio, and diameter
# of a tire

import math

# Calculation of the volume into liters
def calculateVolume(width,aspectRatio,diameter):
    v = math.pi * width * width * aspectRatio * (width * aspectRatio + 2540*diameter)/10000000000
    return v 
    
# Main function that starts working
def main():
    # Request tire parameters
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    aspectRatio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Calculate and format volume...
    vol = calculateVolume(width,aspectRatio,diameter)
    vol = format(vol, ".2f")

    # Output the result
    print("The approximate volume is " + vol + " liters")


# Code that starts main()
if __name__ == '__main__':
    main()
