from data import MENU, resources

order = input("what You want, Espresso, Latte , cappuchino").lower()


def resource_sufficient(order_ingredients):
  for item in order_ingredients:
    if order_ingredients[item] > resources[item]:
      print(f"insufficent item, {item}")
      return False
  return True