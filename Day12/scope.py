level = 10
enemies = ['cat','dog','crow']

def new_enemy():
  newa = ""
  if level > 5:
    newa = enemies[0]
  print(newa)
new_enemy()
print(enemies)
