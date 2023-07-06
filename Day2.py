#subscripting in python; pulling any character from the string
#The below code will extract the character that is at 2nd index "y"
print("Tayyab" [2])

#Python ignores the underscore_ in numbers, output will be 24 
print(1_2 + 1_2)

#You can check the type of data by using type() function
#Following code will print the type of name data type which is string
name = "Tayyab"
print(type(name))    

#Type conversion; converting one data type to another
name_char = len(input("What is your name: "))
new_name_char = str(name_char)
print("Your name has " + new_name_char + " characters.")

#-------------------------------------------------------------------------------   
# 1st coding challenge
# Code challenge: add the user input of two digit number
#-------------------------------------------------------------------------------
new_input = input("Enter a two digit number: ")
sum = int(new_input[0]) + int(new_input[1])
print(sum)

#-------------------------------------------------------------------------------   
# 2nd coding challenge
#-------------------------------------------------------------------------------
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#Write your code below this line 👇
new_height = float(height)
new_weight = float(weight)
result = new_weight / (new_height*new_height)
print(result)

#round function round a number to a given precision in decimal digits.
print(round(2.4424232 , 4))

#or you can use double forward slash to make the result in integer
print( 8 // 3 )

#F-string example
name = "Tayyab"
age = 20
isAlive = True
print(f"My name is {name}, my age is {age} , and it is {isAlive} that I am alive")

#-------------------------------------------------------------------------------   
# 3rd coding challenge
#-------------------------------------------------------------------------------
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
#Write your code below this line 👇
total_age = 90
remaining_age = total_age - int(age)
days = remaining_age * 365
weeks = remaining_age * 52
months = remaining_age * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

#Output
#What is your current age? 20
#You have 29200 days, 4150 weeks, and 936 months left.
