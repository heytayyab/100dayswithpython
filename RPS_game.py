# This code simulates a game of rock, paper, scissors. It asks the user for their choice and then compares it to the computer's choice. It then prints out the result of the game and the scores of each player. The code then asks the user if they want to play again and starts the game over if they do.

# Make this code easier to read, including by adding comments, renaming variables, and/or reorganizing the code.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# The game_images list contains images of a rock, paper, and scissors. The options list contains the numbers 0, 1, and 2. The user_score and computer_score variables keep track of the score of the user and computer, respectively.
game_images = [rock, paper, scissors]
options = [0, 1, 2]
user_score = 0
computer_score = 0

# The while loop keeps the game going until the user decides to stop playing.
while True:
    # Get user's choice
    user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors: "))
    if user_choice not in options:
        print("Invalid input. Please try again.")
        continue

    # Get computer's choice
    computer_choice = random.choice(options)

    # Print the user and computer's choices
    print("You chose:")
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[computer_choice])

    # Calculate the winner
    if computer_choice == user_choice:
        print("That's a tie")
    elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
        print("Computer wins!")
        computer_score += 1
        
    else:
        print("You won")
        user_score += 1

    # Print the user and computer's scores
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again == "n":
        break