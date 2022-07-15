# day 4 - rock paper scissors

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

#Write your code below this line 👇

#create array with ascii graphics
graphics = [rock, paper, scissors]

#get user and computer choices
userChoice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors\n"))
compChoice = random.randint(0,2)

#print choices using some f-strings for brevity
print(f"Your choice:\n{graphics[userChoice]}")
print(f"Computer choice:\n{graphics[compChoice]}")

#decide the winner and print result
if(userChoice == 0):
    if(compChoice == 0):
        print("Tie game.")
    elif(compChoice == 1):
        print("Computer wins.")
    else:
        print("You win.")
elif(userChoice == 1):
    if(compChoice == 0):
        print("You win.")
    elif(compChoice == 1):
        print("Tie game.")
    else:
        print("You lose.")
else:
    if(compChoice == 0):
        print("You lose.")
    elif(compChoice == 1):
        print("You win.")
    else:
        print("Tie game.")
