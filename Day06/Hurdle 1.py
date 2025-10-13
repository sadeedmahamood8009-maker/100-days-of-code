def turn_right():
    turn_left()
    turn_left()
    turn_left()
def full_move():   
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
turn = 6
while turn > 0:
    full_move()
    turn -= 1
    print(turn)
      



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
