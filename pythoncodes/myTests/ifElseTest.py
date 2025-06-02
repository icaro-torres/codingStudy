name = input("What is your name? ")
age = input("What is your age? ")
print("Hello, " + name + ". You are " + age + " years old.")
fruit = input("What is your favorite fruit? ")
print("Your favorite fruit is " + fruit + ", and you are " + age + " years old.")
place = input("Where do you live? ")
print("You live in " + place + ", and your favorite fruit is " + fruit + ".")
print("You are " + age + " years old, and your name is " + name + ".")
if int(age) > 18:
    print("You are an adult.")
else: 
    print("You are a minor.")
if place == "Rio de Janeiro":
    pass
else:
    print("You don't live there.")
print("Thank you for your responses!")
