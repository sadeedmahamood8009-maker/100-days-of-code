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
    
while at_goal() != True:
    full_move()
      



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
