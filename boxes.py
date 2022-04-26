# Cheri Hansen - cherilynne@byui.edu
# Created by 4/25/22
# Week 2 assignment CSE 111-12
"""
 A manufacturing company needs a program that helps employees pack items into boxes for shipping.
"""

# Import the math module so that we can call the math.ceil function.
import math

# Compute the number of item per boxes by dividing and then calling the math. ceil function
# Calculation of number of itemsPerBox by dividuing and item per box.
def getNumOfBoxes(items,itemsPerBox):
    boxes = items//itemsPerBox
    if boxes < 5:
        boxes += 1

    return boxes


# Main function that starts working
def main():
    items = int(input("Enter the number of items: "))
    itemsPerBox = int(input("Enter the number of item per box: "))

    # Get number of boxes
    boxes = getNumOfBoxes(items,itemsPerBox)
    
    # Output results...
    print()
    print(f"For {items} items, packing {itemsPerBox} items in each box, you will need {boxes} boxes.")

# Code that starts main()
if __name__ == '__main__':
    main()
