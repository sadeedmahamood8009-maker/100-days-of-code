import random
from arts import logo

def pick_card():
  card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  random_pick = random.choice(card)
  return random_pick

def calculate_score(card):
  if sum(card) == 21 and len(card) == 2:
    return 0
  if 11 in card and sum(card) > 21:
    card.remove(11)
    card.append(1)
  return sum(card)


def compare(u_score,c_score):
  if u_score == c_score:
    return "DRAW"
  elif c_score == 0:
    return "LOSE, OPPONENT HAVE BLACKJACK"
  elif u_score == 0:
    return "WIN, WITH A BLACKJACK"
  elif u_score > 21:
    return "YOU WENT OUT, YOU LOSE"
  elif c_score > 21:
    return "YOU WIN, OPPONENT WENT OUT"
  elif u_score > c_score:
    return "YOU WIN"
  else:
    return "YOU LOSE"

def play_game():
  print(logo)
  user_card = []
  computer_card = []
  user_score = -1
  computer_score = -1
  in_game_over = False
  for _ in range(2):
    # pick = pick_card()     "we can use either 
    # user_card.append(pick)  this way also."
    user_card.append(pick_card()) 
    computer_card.append(pick_card()) 


  while not in_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print(f"your cards are: {user_card}, score is: {user_score}")
    print(f"computer first card is: {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      in_game_over  = True
    else:
      user_should_deal = input("enter 'y' for another card and enter 'n' for pass: ")
      if user_should_deal == "y":
        user_card.append(pick_card())
      else:
        in_game_over = True


  while computer_score != 0 and computer_score < 17:
    computer_card.append(pick_card())
    computer_score = calculate_score(computer_card)

  print(f"Your final hand: {user_card}, final score: {user_score}")
  print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
  print(compare(user_score,computer_score))


while input("DO YOU WANT TO PALY BLACKJACK, type 'y' or 'n' ") == "y":
  print("\n" * 20)
  play_game()
