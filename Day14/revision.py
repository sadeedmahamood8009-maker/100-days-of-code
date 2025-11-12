import random
from game_data import data
from img import logo, vs

print(logo)
score = 0

def users(account):
  account_name = account["name"]
  account_country = account["country"]
  account_description = account["description"]
  return f"{account_name}, is a {account_description}, from {account_country} "

def correctinfo(user_guess,followers_a,follorers_b):
  if followers_a > follorers_b:
    return user_guess == "a"
  else:
    return user_guess == "b"


account_b = random.choice(data)
game_over = False
while not game_over:
    
  account_a = account_b
  account_b = random.choice(data)

  print(f"Compare A: {users(account_a)}")
  print(vs)
  print(f"Compare B: {users(account_b)}")

  if account_a == account_b:
    account_b = random.choice(data)

  guess = input("Who have more followers, 'A' or 'B' :").lower()

  account_a_follower = account_a["follower"]
  account_b_follower = account_b["follower"]

  activate = correctinfo(guess,account_a_follower,account_b_follower)

  if activate:
    score += 1
    print(f"u got it right, current score:{score}")
  else:
    print(f"u got it wrong, final score:{score}")
    game_over = True



