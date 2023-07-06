print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Tayyab]
*******************************************************************************  
                      ''')


option1 = input("Welcome to the tomb of Dr. Jones! Are you ready to begin your treasure hunt? (Yes/No) \n")
if option1 == "yes" or option1 == "Yes" or option1 == "YES":
    option2 = input("You find yourself in a dimly lit chamber, surrounded by sandstone pillars. Which direction do you want to go? (Left/Right) \n")

    if option2 == "left" or option2 == "Left":
        option3 = input("You come to a statue of Anubis, the god of the dead. What do you want to do? (Inspect the statue/keep walking)\n")
    
        if option3 == "keep walking":
            option4 = input("You find a tapestry hanging on the wall. Do you want to investigate? (Yes/No)\n")
        
            if option4 == "yes":
                print("You find the secret code [python]")
                code_input = input("You enter the hidden chamber and find Dr. Jones' treasure! Enter the secret code: \n")
                
                while True:
                    code_input = input("Enter the correct code: ")
                    if code_input == "python":
                        print("Congratulations, you have completed the treasure hunt!")
                        break
                    else:
                        print("Incorrect code entered. Try again.")

            else:
                print("You reached the end with no treasure, Game Over!")

        else:
            print("A monster eats you, Game Over!")
    else:
        print("You fall into a hole, Game Over!")
else:
    print("Coward man can't get anything, better luck next time!")