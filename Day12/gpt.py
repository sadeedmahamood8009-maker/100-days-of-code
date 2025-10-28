import random
from art import logo
print(logo)
print("WELCOME TO NUMBER GUESSING GAME \n The Number is between 1 to 100")

ran_num = random.randint(1,100)

EASY_MODE = 10
HARD_MODE = 5

def set_difficilty():
  ur_choice = input("Enter the mode, 'hard' or 'easy' : ")
  if ur_choice == 'hard':
    return HARD_MODE
  else:
    return EASY_MODE

def play_game():
  turns = set_difficilty()
  game_over = False

  while not game_over:
    print(f"u have {turns} attempts lest.")
    guess = int(input("Guess the number: "))

    if guess < ran_num:
          print("Too low.")
    elif guess > ran_num:
        print("Too high.")
    else:
        print(f"You win! The number was {ran_num}.")
        game_over = True
        continue
        
    turns -= 1
    if turns == 0:
        print(f"You lose! The number was {ran_num}.")
        game_over = True

play_game()
