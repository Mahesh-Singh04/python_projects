# ----------------------------------------------------------
# Title      : Simple Calculator
# Author     : Mahesh Singh
# Date       : 2025-11-02
# Description: Takes two numbers as input and prints their
#              sum, difference, product, and division.
# ----------------------------------------------------------


num1 = float(input("Enter the first Number:"))
num2 = float(input("Enter the second Number:"))

addition = num1 + num2 
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 !=0 else"indefined (cannot devide by Zero)"

print("\nResults")
print("Sum:",addition )
print("Difference:",subtraction )
print("Product:",multiplication )
print("Division:", division)

