# #This code takes input from user, converts it into list of integers
# #and then calculates the average of the list and prints it.

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# height_sum = 0
# count = 0

# for height in student_heights:
#     height_sum += height
#     count += 1

# print("The average of student heights = ", height_sum // count)
#___________________________________________________________________________________

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# highest_score = 0

# for score in student_scores:
#     if score > highest_score:
#         highest_score = score 

# print(f"The highest score in the class is: {highest_score}" )


#_________________________________________________________________________________
# sum_of_numbers = 0
# for numbers in range(2 , 101 , 2):
#     sum_of_numbers += numbers
# print(sum_of_numbers)

#_________________________________________________________________________________

#THE FIZZ BUZZ GAME 

# for number in range(1 , 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)

#_________________________________________________________________________________

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= random.randint(3 , 6)
nr_symbols = random.randint(4, 8)
nr_numbers = random.randint(3 , 6)



password_list = []

for char in range(1 , nr_letters+1):
    password_list += random.choice(letters)

for char in range(1 , nr_symbols):
    password_list += random.choice(symbols)

for char in range(1 , nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)
print(''.join(password_list))