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
select = int(input("Select\n '1' for rock\n '2' for papper\n '3' for scissor\n CHOOSE:"))
if select == 1:
  print("u choose",rock)
elif select == 2:
  print("u choose",paper)
else:
  print("u choose",scissor) 
list = [rock,paper,scissor]
print("Computer choose",random.choice(list))

if select == 1 and list == rock:
  print("Draw")
# elif rock == paper:

