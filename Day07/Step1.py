import random

word_list = ["lion","fox","tiger","cow"]
random_word = random.choice(word_list)
print(random_word)

letter = input("Enter a letter: ").lower()

for i in (random_word):
  if i == letter:
    print("Right")
  else:
    print("wrong")
