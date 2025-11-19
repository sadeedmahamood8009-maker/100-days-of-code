from data import MENU, resources


def is_resource_sufficient(order_ingredient):
  for item in order_ingredient:
    if order_ingredient[item] > resources[item]:
      print(f"insufficent item, {item}")
      return False
  return True

def insert_coin():
  """total coin inserted"""
  print("Insert Coin:")
  total = int(input("How many quarters: ")) * 0.25
  total += int(input("How many dimes: ")) * 0.10
  total += int(input("How many nickles: ")) * 0.05
  total += int(input("How many pennies: ")) * 0.01
  return total


def is_transition_successful(money_received,drink_cost):
  if money_received >= drink_cost:
    global profit
    change = round(money_received - drink_cost,2)
    print(f"Here the ${change} change")
    profit += drink_cost
    return True
  else:
    print("sorry that's not enought money, money refunded!")
    return False


def make_coffee(drink_name, order_ingredient):
  for item in order_ingredient:
    resources[item] -= order_ingredient[item]
  print(f"Here is your {drink_name}☕")

profit = 0
machine_on = True
while machine_on:
  order = input("what would u like, (espresso/latte/cappuchino): ").lower()
  if order == "off":
    machine_on = False
  elif order == "report":
    print(f"water : {resources['water']}ml")
    print(f"milk : {resources['milk']}ml")
    print(f"coffee : {resources['coffee']}g")
    print(f"money : ${profit}")
  else:
    drink = MENU[order]
    # print(drink)
    if is_resource_sufficient(drink['ingrediends']):
      payment = insert_coin()
      if is_transition_successful(payment,drink["cost"]):
        make_coffee(order, drink["ingrediends"])