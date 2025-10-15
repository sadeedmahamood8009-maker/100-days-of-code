import random
from hangman_words import word_list
from hangman_arts import stage
from hangman_logo import logo


lives = 0
print(logo)
# word_list = ["lion","fox","tiger","cow"]
random_word = random.choice(word_list)
print(random_word)

placeholder = "_"
len_word = len(random_word)
for i in range (len_word):
  print(end=placeholder)

correct_letter = []
game_over = False
while not game_over:
  print(f"\nyou got {lives}/6 left")
  letter = input("\nEnter a letter: ").lower()
  display = " "

  if letter in correct_letter:
    print(f"you already guessed the letter,{letter}")

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
    print("***************YOU WIN**************")

  if letter not in random_word:
    lives += 1
    print(f"you guessed {letter}, thats not in the word you lose a life")
    if stage == 6:
      game_over = True
      print(f"********************IT WAS {random_word},YOU LOSE******************")
  print(stage[lives])

