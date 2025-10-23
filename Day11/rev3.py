import random

def pick_card():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  random_card = random.choice(cards)
  return random_card


def calculate_sroce(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

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
  user_card = []
  computer_card = []
  game_over = False

  for _ in range(2):
    user_card.append(pick_card())
    computer_card.append(pick_card())

  while not game_over:
    user_score = calculate_sroce(user_card)
    computer_score = calculate_sroce(computer_card)
    print(f"user cards are :{user_card}, and score is :{user_score}")
    print(f"computer first card is: {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      game_continue = input("type 'y' to pick another card, and type 'n' to end the game")
      if game_continue == 'y':
        user_card.append(pick_card())
      else:
        game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_card.append(pick_card())
    computer_score = calculate_sroce(computer_card)

  print(f"Your hand {user_card}, final score {user_score}")
  print(f"Your hand {computer_card}, final score {computer_score}")
  print(compare(user_score, computer_score))
while input("do you need a start a new game, 'y' or 'n' ") == 'y':
  print("\n" * 20)
  play_game()