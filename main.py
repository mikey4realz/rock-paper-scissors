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
player_choice = int(input("ROCK, PAPER, SCISSORS, SHOW!!! Type 0 for Rock, 1, for Paper, 2 for Scissors:\n"))
computer_choice = random.randint(0,2)
choices = [rock,paper,scissors]

if(player_choice != 0 and player_choice != 1 and player_choice != 2):
  print("ERROR! You have chosen an invalid choice. A choice be will chosen for you at random.\n\n")
  player_choice = random.randint(0,2)

print(f"\nYou: {choices[player_choice]}\nvs\n\nComputer: \n{choices[computer_choice]}")

if player_choice == 0 and computer_choice == 2: #Rock Beats Paper
  print("You Win!")
elif computer_choice == 0 and player_choice == 2: #Rock Beats Paper
  print("You Lose.")
elif player_choice > computer_choice: #Paper Beats Rock, Scissors beats Paper
  print("You Win!")
elif player_choice == computer_choice:
  print("It is a Draw.")
else:
  print("You Lose.")

