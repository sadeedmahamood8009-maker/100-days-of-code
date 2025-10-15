import random

word_list = ["lion","fox","tiger","cow"]
random_word = random.choice(word_list)
print(random_word)
placeholder = "_"
len_word = len(random_word)
for i in range (len_word):
  print(end=placeholder)

letter = input("\nEnter a letter: ").lower()
display = " "
for i in (random_word):
  if i == letter:
    display += i
    print("Right")
  else:
    display += "_"
    print("wrong")
print(display)