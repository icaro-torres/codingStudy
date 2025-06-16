# this code is a simple while loop that prints numbers from 1 to 10.
'''
x = 1
while x <= 10:
    print(x)
    x = x + 1
'''

'''
end = int(input("Enter the end number: "))
# this code prints all numbers from 1 to a user-defined end number.
x = 1
while x <= end:
    print(x)
    x = x + 1
'''

# this code prints all numbers from 1 to a user-defined end number that are divisible by 4.
'''
end = int(input("Enter the end number: "))
x = 1
while x <= end:
    if x % 4 == 0:
        print(x)
    x = x + 1

'''

# sum of numbers entered by the user until they enter a specific number.
'''
end = int(input("Enter the end number: "))
x = 1
plus = 0
while x <= end: 
    plus = plus + x # accumulate the sum
    x = x + 1  # increment the counter
print("The sum of numbers from 1 to ", end, "is: ", plus)
'''

# this code calculates the average of 4 numbers entered by the user and prints the avarage between them.
'''
x = 1
sum = 0
while x <= 4:
    n = int(input("Enter a number {x}: "))
    sum = sum + n  # accumulate the sum of numbers entered by the user
    x += 1  # increment the counter
avarage = sum / 4  # calculate the average
print("The average of the numbers entered is: ", avarage)
'''

# so, this code counts how many even numbers were entered by the user until they enter 10, which stops the loop. the variable `qtde` is incremented each time an even number is entered. the final count is printed after the loop ends.
# if the condition isn't met, the loop continues to ask for a number until the user enters 10. this is a simple way to count even numbers in a user input scenario.
'''
qtde = 0
while True:
    n = int(input("Enter a number (10 to stop): "))
    if n == 10:
        break # stop the loop if 10 is entered
    if n % 2 == 0: # check if the number is even
        qtde += 1 # increment the count of even numbers
print("The number of even numbers entered is: ", qtde)
'''

# this code prints a multiplication table from 1 to 10 using nested while loops. the outer loop iterates through the multiplication tables (1 to 10), and the inner loop iterates through the numbers (1 to 10) for each multiplication table.
'''
multiplication_table = 1
while multiplication_table <= 10: # outer loop for multiplication tables
    number = 1  #  reset the number for each multiplication table
    while number <= 10: # inner loop for numbers in each multiplication table
        value = multiplication_table * number # calculate the product
        print(f"{multiplication_table} x {number} = {value}") # print the multiplication result
        number += 1  # increment the number for the next multiplication
    multiplication_table += 1 # increment the multiplication table for the next iteration
print("Complete multiplication table!")
'''

'''
for multiplication_table in range(1, 11):
    for number in range(1, 11):
        value = multiplication_table * number
        print(f"{multiplication_table} x {number} = {value}")
'''

'''
for x in range(1, 12):
    if x % 2 == 0:
        print(f"{x} is even, skipping...")
        continue
    if x == 10:
        break
    print(x)
'''

# this is a exercise that prints the first 100 numbers divided by 2, starting from 1. it increments the number by 1 in each iteration and prints the result of the division. the teacher asked what was the error of the code (the original was n = 1, while n <= 100: print(n/2)) without the increment n += 1, which would cause an infinite loop. it doesn't take me a long time to figure it out, tho.
'''
n = 1
while n <= 100:
    n += 1
    print(n/2)
'''

# this exercise prompts the user to enter a number and calculates its square and square root. the loop continues until the user enters 0, at which point it exits the loop and prints a message indicating that the loop has ended. this was taking a while to figure out, but i finally got it right.
'''
import math

n = 0
while True:
    n = int(input("Enter a number (0 if you want to stop): "))
    if n == 0:
        print("Exiting the loop.")
        break
    else:
        square = n ** 2
        square_root = math.sqrt(n)
        print(f"The square of {n} is {square} and the square root is {square_root:.2f}.")
print("Loop ended.")
'''

lines = int(input("Enter the number of lines: "))
columns = int(input("Enter the number of columns: "))
for i in range(1, lines + 1):
    for j in range(1, columns + 1):
        print("#", end="")
    2
    print()  # print a new line after each row