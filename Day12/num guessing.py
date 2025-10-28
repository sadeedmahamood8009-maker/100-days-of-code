import random
print("WELCOME TO NUMBER GUESSING GAME! \nThe Number is between 1 to 100")

numbers = list(range(1,100))
ran_num = random.choice(numbers)
print(ran_num)
game_over = False

easy = 10
hard = 5

def set_defficulty():
  select_mode = input("select 'easy' or 'hard' mode!!")
  if select_mode == 'hard':
    return hard
  else:
    return easy
  

while not game_over:
  enter_num = int(input("Guess the number: "))
  turn = set_defficulty()
  print(f"u got {turn} left")
  def num():
    if enter_num < ran_num:
      print(f"{enter_num} to low")
    elif enter_num > ran_num:
      print(f"{enter_num} to high")
    else:
      print("you win")
      game_over = True
  num()
