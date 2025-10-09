import random

# coin=int(input("Select '0' for HEAD or '1' for TAIL :"))
# game=random.randint(0,1)
# if game == 0:
#   print("HEAD")
# else:
#   print("TAIL")
# print(game)
# if game == coin:
#   print("YOU WIN")
# else:
#   print("YOU LOSE")


coin=input("Select HEAD or TAIL :")
game=random.randint(0,1)
if game == 0:
  result = "HEAD"
else:
  result = "TAIL"
print(result)
if coin.upper() == result:
  print("YOU WIN")
else:
  print("YOU LOSE")