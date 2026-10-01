import random

Rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [Rock, Paper, Scissor]
user_choice = int(input("what do you choose? Type 0 for rock, 1 for paper, 2 for scissors \n") )
if user_choice >=0 and user_choice <=2:
    print("you choose")
    print(game[user_choice])
computer_choice = random.randint(0, 2)
print("computer choose")
print(game[computer_choice])
if user_choice >= 3 or user_choice < 0:
    print("you typed invalid number.  you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice ==  user_choice:
    print("it's a draw")

