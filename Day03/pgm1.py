print("welcome to pizza delivery")
size = input("what size pizza do u want? S,M or L::")
bill=0
if size == "S":
  bill=15
  print("u selected Small pizza")
elif size == "M":
  bill=20
  print("u selected medium pizza")
elif size == "L":
  bill=25
  print("u selected Large pizza")
else:
  print("there is no such a pizza")
pepperoni = input("Do u need pepperoni on your pizza? Y or N:")
if pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
cheese = input("do u need extra cheese? Y or N:")
if cheese == "Y":
  bill += 1
print(f"total bill is {bill}")


 

