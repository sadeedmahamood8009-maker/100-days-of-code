import random

word_list = ["lion","fox","tiger","cow"]
random_word = random.choice(word_list)
# print(random_word)
placeholder = "_"
len_word = len(random_word)
for i in range (len_word):
  print(end=placeholder)
correct_letter = []
game_over = False
while not game_over:
  letter = input("\nEnter a letter: ").lower()
  display = " "
  for i in (random_word):
    if i == letter:
      display += i
      correct_letter.append(i)
    elif i in correct_letter:
      display += i
    else:
      display += "_"
  print(display)
  if "_" not in display:
    game_over = True
    print("YOU WIN")

