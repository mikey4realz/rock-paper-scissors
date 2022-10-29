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
player_choice = int(input("ROCK, PAPER, SCISSORS!!! Type 0 for Rock, 1, for Paper, 2 for Scissors:\n"))
computer_choice = random.randint(0,2)
choices = [rock,paper,scissors]

print(f"You: {choices[player_choice]}\nvs\n\nComputer: \n{choices[computer_choice]}")

if player_choice == 0 and computer_choice == 2:
  print("You Win!")
elif player_choice > computer_choice:
  print("You Win!")
else:
  print("You Lose.")

