import random
from game_data import data
from img import logo, vs

print(logo)
score = 0
game_over = False

account_b = random.choice(data)
while not game_over:
  
  def formate_data(account):
    name_account =account ["name"]
    description_account = account["description"]
    country_account = account["country"]
    return f"{name_account}, is a {description_account},from {country_account}"


  def check_answer (user_guess, a_follower,b_follower):
    if a_follower > b_follower:
      if user_guess == "a":
        return True
      else:
        return False
    else:
      if user_guess == "b":
        return True
      else:
        return False
  # def check_answer (user_guess, a_follower,b_follower):
  #   if a_follower > b_follower:
  #     return user_guess == "a"
  #   else:
  #     return user_guess == "b"
  account_a = account_b
  account_b = random.choice(data)

  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {formate_data(account_a)}")
  print(vs)
  print(f"Compare B: {formate_data(account_b)}")


  guess = input("Who has more followers select 'A' or 'B': " ).lower()

  print("\n" * 20)
  print(logo)

  follower_account_a = account_a["follower"]
  follower_account_b = account_b["follower"]
  is_correct = check_answer(guess, follower_account_a, follower_account_b)

  if is_correct:
    score += 1
    print(f"You got it right, current score :{score}")
  else:
    print(f"YOU got it wrong, final score :{score}")
    game_over = True
