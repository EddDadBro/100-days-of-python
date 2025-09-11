def forward():
    if wall_in_front():
        turn_left()
    elif not object_here():
        move()
    else:
        take()
            
def start():
    move()

start()
while not at_goal():
    forward()

        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
