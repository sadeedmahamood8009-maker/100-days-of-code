import random
def pick_card():
  card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  random_pick = random.choice(card)
  return pick_card

user_card = []
computer_card = []
for _ in range(2):
  # pick = pick_card()     "we can use either 
  # user_card.append(pick)  this way also."
  user_card.append(pick_card()) 
  computer_card.append(pick_card()) 


def calculate_score(card):
  if sum(card) == 21 and len(card) == 2:
    return 0
  if 11 in card and sum(card) > 21:
    card.remove(11)
    card.append(1)
  return sum(card)
# calculate_score([11, 10])   # Ace + 10 → Blackjack → returns 0
# calculate_score([11, 9, 5]) # 25 → change Ace → [1, 9, 5] → 15
# calculate_score([3, 8, 10]) # Just adds up → 21