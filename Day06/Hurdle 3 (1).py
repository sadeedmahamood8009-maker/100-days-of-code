def turn_right():
    turn_left()
    turn_left()
    turn_left()

def clear():
    if fornt_is_clear():
        move()
def wall():
    elif wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
while not at_goal():
    clear()
    wall()
        
        
        




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
