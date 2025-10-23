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

user_card = []
computer_card = []
game_over = False

for _ in range(2):
  user_card.append(pick_card())
  computer_card.append(pick_card())

user_score = calculate_sroce(user_card)
computer_score = calculate_sroce(computer_card)
print(f"user cards are :{user_card}, and score is :{user_score}")
print(f"computer first card is: {computer_card[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
  game_over = True
