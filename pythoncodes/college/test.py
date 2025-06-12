#studying if-else commands in python in my college

'''
x = int(input("Enter a number: "))

if x >= 10:
    print("The number is greater than or equal to 10.")	
if x < 10:
    print("The number is less than 10.")

print(f"You entered: {x}")
'''

# i added the if statement to check the value of x

'''
a = int(input("Enter your age: "))
if a >= 18:
    print("You are an adult.")
    print("You can drive.")
else:
    print("You are a minor.")
    print("You cannot drive.")
'''

# in the books i have this exercise to do: write a program that calculates the price to be paid for electricity, based on the amount of kWh consumed and the type of installation (R for residential, I for industrial and C for commercial). the price is giving according to the following table:
# R - up to 500: R$ 0.40, over 500: R$ 0.65
# I - up to 1000: R$ 0.55, over 1000: R$ 0.60   
# C - up to 5000: R$ 0.55, over 5000: R$ 0.60

kWh = int(input("Enter the amount of kWh consumed: "))
installation = input("Enter the type of installation (R, I, C): ")
price = 0.0

if installation == 'R':
    if kWh <= 500:
        price = 0.40
    else:
        price = 0.65
elif installation == 'I':
    if kWh <= 1000:
        price = 0.55
    else:
        price = 0.60
elif installation == 'C':
    if kWh <= 5000:
        price = 0.55
    else:
        price = 0.60

total = kWh * price
print(f"The total price to be paid for electricity is: R$ {total}.")

# this code calculates the price to be paid for electricity based on the amount of kWh consumed and the type of installation.

# i could do the last one likke this too:
'''
elif kWh <= 5000:
        price = 0.55
    else:
        price = 0.60
'''
# but i prefer the first one because it is more readable and easier to understand.