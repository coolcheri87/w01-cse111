# Cheri Hansen - cherilynne@byui.edu
# Created 4/30/2022
# Week 2 Assignment - CSE111-12
# Create a function that calculates volume from width, aspect ratio, and diameter
# of a tire and records each try of the program.

from datetime import datetime
import math

# Calculation of the volume into liters
def calculateVolume(width,aspectRatio,diameter):
    v = math.pi * width * width * aspectRatio * (width * aspectRatio + 2540*diameter)/10000000000
    return v 

def recordEntry(width,aspectRatio,diameter,vol):
    ts = datetime.now() # timestamp

    # Open a text file named cities.txt in append mode.
    with open("volumes.txt", "at") as volumes_file:
         print(f"{ts:%Y-%m-%d}, {width}, {aspectRatio}, {diameter}, {vol}", file=volumes_file)
   
    
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

    # record this try...
    recordEntry(width,aspectRatio,diameter,vol)
    


# Code that starts main()
if __name__ == '__main__':
    main()
