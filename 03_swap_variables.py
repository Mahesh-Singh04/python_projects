# ----------------------------------------------------------
# Title      : Swap Two Variables (Without Third Variable)
# Author     : Mahesh Singh
# Date       : 2025-11-02
# Description: Takes two numbers as input and swaps them
#              without using a temporary variable.
# ----------------------------------------------------------

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print(f"\nBefore swapping: a = {a}, b = {b}")

# Swapping using tuple unpacking (best Pythonic way)
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")
print("Values swapped successfully!")
