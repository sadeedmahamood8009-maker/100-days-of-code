import random
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
     ''' )

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''' )
scissor = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
      ''' )
game_image = [rock,paper,scissor]
user_choice = int(input("user_choice\n '0' for rock\n '1' for papper\n '2' for scissor\n CHOOSE:"))
print(f"user choice :{user_choice}")
print(game_image[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer choice :{computer_choice}")
print(game_image[computer_choice])

if user_choice >2:
  print("there is no such an option,YOU LOSE!")
elif user_choice == computer_choice:
  print("Draw")
elif user_choice == 0 and computer_choice == 2:
  print("You Won")
elif computer_choice == 0 and user_choice == 2:
  print("You Lose")
elif user_choice > computer_choice:
  print("You Win")
elif computer_choice > user_choice:
  print("You Lose")