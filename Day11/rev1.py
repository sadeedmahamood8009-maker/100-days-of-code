import random

def pick_card():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  random_card = random.choice(cards)
  return random_card

user_card = []
computer_card = []

for _ in range(2):
  user_card.append(pick_card())
  computer_card.append(pick_card())
print(user_card)
print(computer_card)
