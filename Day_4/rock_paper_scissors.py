
import random

# Rock Paper Scissors ASCII Art
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
---'    ____)____
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

game_image = [rock, paper, scissors]
# user choice
user_choice = int(input(f"what do you choose? 0 for rock, 1 for paper, 2 for scissors: \n "))
if user_choice in range(3):
    print(game_image[user_choice])
# computer choose
computer_choice = random.randint(0,2)
print(f"computer choice {game_image[computer_choice]}")
# logic to decide a winner!
if user_choice not in range(3):
    print(f"you entered invalid choice, please try again")
elif user_choice == 0 and computer_choice == 2:
    print(f"You Win!")
elif computer_choice == 0 and user_choice == 2:
    print(f"You Lose!")
elif user_choice > computer_choice:
    print(f"You Win!")
elif user_choice < computer_choice:
    print(f"You Lose!")
elif user_choice == computer_choice:
    print(f"It's a Draw!")




