# this code calculates the square root of the sum of squares of two numbers

import math # importing the math module

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = math.sqrt(a**2 + b**2)

print("The square of the first number is:", a**2)
print("The square of the second number is:", b**2)
print("The square root of the sum of squares is:", c)
# it prompts the user to input two numbers, computes the square root of the sum of their squares and prints the results

# i wasn't wrong tho, but i can print it like this:
print(f"The square root of the sum of squares of {a} and {b} is: {c}")