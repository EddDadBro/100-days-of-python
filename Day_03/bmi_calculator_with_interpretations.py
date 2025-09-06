weight = int(input("What is your current weight? "))
height = float(input("What is your height? "))
bmi = weight / (height **2)
rounded_bmi = round(bmi, 2)
print(f"Your BMI is " + str(rounded_bmi))
if bmi >= 25:
    print("You are overweight.")
elif bmi < 25:
    print("You are at a normal weight!")
else:
    print("You are underweight.")
