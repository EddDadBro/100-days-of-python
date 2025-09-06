print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Your ticket price is $5, please! ")
    elif age <= 18:
        print("Your ticket price is $7, please! ")
    elif age < 65:
        print("Your ticket price is $12, please! ")
    else:
        print("You get the senior citizen discount! $4, please!")
else:
    print("Sorry you have to grow taller before you can ride.")
