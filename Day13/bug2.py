try:
  age = int(input("Enter your age: "))
except ValueError:
  age = int(input("Enter your age: "))

if age >= 18:
  print(f"You can eligible for taking license cuz you {age} age")
