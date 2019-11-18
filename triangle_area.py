#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program calculates the area of triangle usinf functions


def calculate_area(base_of_triangle, height_of_triangle):
    # This function calculates the area of the triangle

    area = (base_of_triangle*height_of_triangle)/2
    print("area of triangle = ", area)


def main():
    # This function gets input from the user

    while True:
        base = input("Enter the base of the triangle: ")
        height = input("Enter the height of the triangle: ")
        print("")
        try:
            base_check = float(base)
            height_check = float(height)

            calculate_area(base_check, height_check)
            break
        except Exception:
            print("Invalid Number ")
            print("")


if __name__ == '__main__':
    main()
