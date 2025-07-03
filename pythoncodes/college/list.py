# this code calculates the average temperature from a list of temperatures using a while loop
'''
temperatures = [25, 18, 12, 22]
sum = 0
n = 0
while n <= 3:
    sum += temperatures[n]
    n += 1
average  = sum / 4
print("The average temperature is: ", average)
'''

# --------------------------
'''
temperatures = [25, 18, 12, 22]
size = len(temperatures)
sum = 0
n = 0
while n <= size - 1:
    sum += temperatures[n]
    n += 1
average  = sum / size
print("The average temperature is: ", average)
'''
# --------------------------

# so, i did a version with for loop because it is more simple, i don't need to use a variable to control the loop and don't need to check the condition of the loop
'''
temperatures = [25, 18, 12, 22]
size = len(temperatures)
sum = 0
for t in temperatures:
    sum += t
    average = sum / size
print("The average temperature is: ", average)
'''
# it still needs the accumulation variable to calculate the sum, but it is more simple than the while loop version

# --------------------------
'''
temperatures = [] # create an empty list to store temperatures
while True:
    t = int(input("Type a temperature (or 0 to stop): "))
    if t == 0:
        break
    temperatures.append(t) # this is the first loop to get the temperatures from the user until the user types 0. every value is added to the list
size = len(temperatures)
sum = 0
for t in temperatures:
    sum += t
average = sum / size # the rest of the code is the same, it calculates the average temperature
print(f"The average temperature is: {average}.")
'''
# --------------------------
'''
list = [40, 20, 60, 10]
value = int(input("Type a value to search in the list: "))
find = False
for i in list:
    if i == value:
        find = True
        break
if find:
    print(f"The value {value} was found in the list.")
else:
    print(f"The value {value} was not found in the list.")
'''
# --------------------------
'''
list = [40, 20, 60, 10]
value = int(input("Type a value to search in the list: "))
find = value in list  # this is a more simple way to check if the value is in the list
if find:
    print(f"The value {value} was found in the list.")
else:
    print(f"The value {value} was not found in the 
'''
# ---------------------------
'''
arroz = ["arroz", 5, 8.5]
feijao = ["feijao", 3, 9.0]
compras = [arroz, feijao]
for item in compras:
    print(f"Item: {item[0]}, Quantity: {item[1]}, Price: {item[2]}")  # this prints the item, quantity and price of each item in the list compras
    
arroz = ["arroz", 5, 8.5]
feijao = ["feijao", 3, 9.0]
compras = [arroz, feijao]
for item in compras:
    for x in item:
        print(x, end=" ")  # this prints the item, quantity and price of each item in the list compras, but in a single line
    print()  # this prints a new line after each item
'''
# ---------------------------
'''
lines = 2
columns = 2
matrix = []
for l in range(lines):
    lines_alocated = [0] * columns  # create a list with the number of columns
    matrix.append(lines_alocated)  # add the list to the matrix
for l in range(lines):
    for c in range(columns):
        value = int(input(f"Type a value: "))
        matrix[l][c] = value  # add the value to the matrix
for l in range(lines):
    for x in range(columns):
        print(matrix[l][x], end=" ")  # print the matrix in a single line
    print()  # print a new line after each line of the matrix
'''
# ---------------------------
'''
lines = 2
columns = 2
matrix = []
for l in range(lines):
    lines_alocated = [0] * columns
    matrix.append(lines_alocated)
for l in range(lines):
    for c in range(columns):
        value = int(input(f"Type a value: "))
        matrix[l][c] = value
qtde = 0
for l in range(lines):
    for c in range(columns):
        if matrix[l][c] > 10:
            qtde += 1  # count how many values are greater than 10
print(f"The number of values greater than 10 is: {qtde}.")
'''
# ---------------------------

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum = [0, 0, 0]  # create a list to store the sum of each column
# read the matrix values
for l in range(3):
    for c in range(3):
        value = int(input(f"Type a value: "))
        matriz[l][c] = value
# the next step is to calculate the sum of each column
# we will use a for loop to iterate through the columns and a nested for loop to iterate through the lines
for c in range(3):
    s = 0 # keep the sum of each column
    for l in range(3):
        s += matriz[l][c]  # sum the values of each column
    sum[c] = s  # store the sum of each column in the sum list
print(sum)