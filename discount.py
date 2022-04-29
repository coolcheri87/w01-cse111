# Cheri Hansen - cherilynne@byui.edu
# Created 4/28/2022
# Week 1 Assignment - CSE111-12
# Create a program that calculates best heart rates for exercise

# Import the datatime class from the datetime
# module so taht it can be used inthis program.
from datetime import datetime


def calculateBill(subtotal):
    discount = 0
    # Calculate day of week - 0 = Monday, 6 = Sunday
    if ((datetime.today().weekday()>=1) and (datetime.today().weekday()<=2)):
        discount = 0.10 * subtotal
        tax = (subtotal-discount)*.06
        total = subtotal-discount+tax
        print(f"Subtotal {subtotal:,.2f}: Discount {discount:,.2f}: Tax {tax:,.2f}: Total {total:,.2f}")
    else:
        tax = subtotal*.06
        total = subtotal + tax
        print(f"Subtotal {subtotal:,.2f}: Tax {tax:,.2f}: Total {total:,.2f}")

def main():
    subtotal = float(input('Subtotal cost: '))
    calculateBill(subtotal)


# Code that starts main()
if __name__=='__main__':
    main()