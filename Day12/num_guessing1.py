import random

easy = 10
hard = 5
turns = 0

def num(user_guess,actual_guess):    
    enter_num = int(input("Guess the number: "))
    turn = set_defficulty()
    if enter_num < ran_num:
      print(f"{enter_num} to low")
      turns -= 1
    elif enter_num > ran_num:
      print(f"{enter_num} to high")
      turns -= 1
    else:
      print("you win")

def set_defficulty():
  select_mode = input("select 'easy' or 'hard' mode!!")
  if select_mode == 'hard':
    return hard
  else:
    return easy
  
