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

choices = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print("You chose: \n", choices[player_choice])

computer_choice = random.randint(0, 2)
print("Computer chose: \n", choices[computer_choice])

if player_choice == computer_choice:
    print("You draw.")

elif computer_choice == 0:
    if player_choice == 1:
        print("You win!")
    elif player_choice == 2:
        print("You lose!")

elif computer_choice == 1:
    if player_choice == 0:
        print("You lose!")
    elif player_choice == 2:
        print("You win!")

elif computer_choice == 2:
    if player_choice == 0:
        print("You win!")
    elif player_choice == 1:
        print("You lose!")
