## volume.py Volume calculations with torus
# Author: brightkoech
# Date: 10-11-2021
from math import pi


def main():
    radius = float(input("Enter the radius of the torus: "))
    height = float(input("Enter the height of the torus: "))
    conevol = 1 / 3 * pi * radius ** 2 * height
    cylvol = pi * radius ** 2 * height
    spherevol = 4 / 3 * pi * radius ** 3
    print("The volume of the cone is: ", conevol)
    print("The volume of the cylinder is: ", cylvol)
    print("The volume of the sphere is: ", spherevol)


main()
