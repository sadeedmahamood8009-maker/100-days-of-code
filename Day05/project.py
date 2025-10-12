import random

letter = ["a","b","c","d","e","f","g"]
digit = ["1","2","3","4","5"]
symbol = ["!","@","#","%"]

print("WELCOME TO PASSWORD GENERATOR")
no_letter = int(input("How many letter :"))
no_digit = int(input("How many digit :"))
no_symbol = int(input("How many symbol :"))

password = []

for i in range(1, no_letter + 1):
  random_letter = random.choice(letter)
  password.append(random_letter)
for j in range(1, no_digit + 1):
  random_digit = random.choice(digit)
  password.append(random_digit)
for k in range(1, no_symbol + 1):
  random_symbol = random.choice(symbol)
  password.append(random_symbol)

print(password)
random.shuffle(password)
print(password)
passw = " "
for n in password:
  passw += n
print(f"the password is {passw}")

