import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
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

if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)

print("Computer chose: ")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if player_choice == 0:
    if(computer_choice == 0):
        print("It's a draw!")
    elif computer_choice == 1:
        print("You Lose!")
    elif computer_choice == 2:
        print("You win!")
elif player_choice == 1:
    if(computer_choice == 1):
        print("It's a draw!")
    elif computer_choice == 2:
        print("You Lose!")
    elif computer_choice == 0:
        print("You win!")
elif player_choice == 2:
    if(computer_choice == 2):
        print("It's a draw!")
    elif computer_choice == 0:
        print("You Lose!")
    elif computer_choice == 1:
        print("You win!")