# Cheri Hansen - cherilynne@byui.edu
# Created 4/21/2022
# Week 1 Assignment - CSE111-12
# Create a function that calculates volume from width, aspect ratio, and diameter
# of a tire

import math

# Calculation of the volume into liters
def calculateVolume(width,aspectRatio,diameter):
    v = math.pi * width * width * aspectRatio * (width * aspectRatio + 2540*diameter)/10000000000
    return str(v)

# Main function that starts working
def main():
    # Request tire parameters
    width = float(input("Input width (millimeters): "))
    aspectRatio = float(input("Input aspect ratio (1-99): "))
    diameter = float(input("Input diameter (inches): "))

    # Calculate and output volume...
    print("Volume = " + calculateVolume(width,aspectRatio,diameter) + " liters")


# Code that starts main()
if __name__ == '__main__':
    main()
