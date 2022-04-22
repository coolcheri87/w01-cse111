# Cheri Hansen - cherilynne@byui.edu
# Created 4/21/2022
# Week 1 Assignment - CSE111-12
# Create a program that calculates best heart rates for exercise

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

# Get the user's age and convert to an integer
age = int(input("Please enter your age: "))

# Compute the slowest and fastest heart rates
max_rate = 220 - age
slowest = str(int(max_rate * 0.65))
fastest = str(int(max_rate * 0.85))

# Output heart rates...
print("When you exercise to strengthen your heart, you should")
print("keep your heart rate between " + slowest + " and " + fastest)
print("beats per minute.")