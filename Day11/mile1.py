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

