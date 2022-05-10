# Group 6: Team Activity
# May 9 2022

import math


def main():
    # Call the storage_efficiency function to compute
    # the volume of an surface_area.
    radius = 2.8
    height = 3.2
    volume = pi*radius**2*height
    surface_area = 2*pi*radius*(radius + height)
    storage_efficiency = volume/surface_area


    # Print several lines that describe this program.
    print(f"#1 Picnic ")
    print("circular cone. For example, if the radius of a")
    print(f"cone is {ex_radius} and the height is {ex_height}")
    print(f"then the volume is {ex_vol:.1f}")
    print()
      # Get the radius and height of the cone from the user.
    radius = float(input("Please enter the radius of the cone: "))
    height = float(input("Please enter the height of the cone: "))

    # Call the cone_volume function to compute the volume
    # for the radius and height that came from the user.
    vol = cone_volume()

    # Print the radius, height, and
    # volume for the user to see.
    print(f"Radius: {radius}")
    print(f"Height: {height}")
    print(f"Volume: {vol:.1f}")

def compute_volume(radius, height):
    """Compute and return the volume of a right circular cone."""
    volume = math.pi * radius**2 * height / 3
    return volume

def compute_surface_area(radius, height):
    """Compute and return the volume of a right circular cone."""
    volume = math.pi * radius**2 * height / 3
    return volume

def compute_storage_efficiency(radius, height):

def compute_volume(radius, height):

def compute_surface_area(radius, height):

    

def
# Start this program by
# calling the main function.

# Start this program by
# calling the main function.
main()