#Randomization and python lists
# This code generates a random float and a random integer. It also prints "Hello World"

import random

# Generate a random float
random_float = random.uniform(1, 4)
# random_float = (random_float % 4) + 1
print(random_float)

# Generate a random integer
random_int = random.randint(1, 4)
print(random_int)

#random float that prints number b/w 0.1 to 0.9999
new_float = random.random()
print(new_float)

# Who is going to buy the meal program
# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# x = len(names)
# choose = random.randint(0 , x-1)
# print(names[choose], "is going to buy the meal today!")
