print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

def check_height(height):
    if height >= 120:
        return True
    else:
        return False

def check_age(age):
    if age < 12:
        return 5
    elif age <= 18:
        return 7
    else:
        return 12

if check_height(height):
    print("You can ride the rollercoaster!")
    age = int(input("What is your age: "))
    print(f"Please pay ${check_age(age)}.")
else:
    print("Sorry! you have to grow taller before  you can ride rollercoaster.")

#-------------------------------------------------------------------------------------
#One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")

#One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#-------------------------------------------------------------------------------------

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height * height)
bmi = round(bmi)

if bmi <= 18.5 :
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")