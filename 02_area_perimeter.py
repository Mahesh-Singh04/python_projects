# ----------------------------------------------------------
# Title      : Area and Perimeter of a Rectangle
# Author     : Mahesh Singh
# Date       : 2025-11-02
# Description: Takes length and width as input and calculates
#              the area and perimeter of a rectangle.
# ----------------------------------------------------------

val1 = float(input("Enter the length of rectangle:"))
val2 = float(input("Enter the width of the rectangle:"))

if val1 <= 0 or val2 <= 0:
    print("Error: length and width must be positive numbers.")
else:
    area = val1 * val2
    perimeter = 2*(val1 + val2)
    print("\nArea of rectangle:",area)
    print("Perimeter of rectangle:", perimeter)