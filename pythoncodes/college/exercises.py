# exercise 1: calculate the average temperature and count how many temperatures are greater than or equal to 15 degrees. the program will ask the user to input 10 temperatures.

temperature = []
total = 0
count = 0
for i in range(10):
    temp = float(input(f"Enter temperature: "))
    temperature.append(temp)
    total += temp
    if temp >= 15:
        count += 1
average = total / len(temperature)
print(f"The average temperature is: {average}")
print(f"Number of temperatures ≥ 15 degrees: {count}")

# exercise 2: create a program that asks the user for their name, age, and email. the program will then create a dictionary with these values and print it.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")
pessoa= {"nome": name, "idade": age, "email": email}
for key, value in pessoa.items():
    print(f"{key}: {value}")

# exercise 3: create a program that asks the user to enter food items they can eat and food items their friend can eat. the program will then find the common food items that both can eat and print them.

my_list = []
while True:
    food1 = input("Enter a food item that you can eat (or press Enter to finish): ")
    if food1 == "":
        print("You have finished entering food items.")
        break
    else:
        my_list.append(food1)

friend_list = []
while True:
    food2 = input("Enter a food item that your friend can eat (or press Enter to finish): ")
    if food2 == "":
        print("You have finished entering food items.")
        break
    else:
        friend_list.append(food2)

common_foods = set(my_list) & set(friend_list)
if common_foods:
    print("You and your friend can eat the following foods together:")
    for food in common_foods:
        print(food)
else:
    print("There are no common foods that you and your friend can eat together.")