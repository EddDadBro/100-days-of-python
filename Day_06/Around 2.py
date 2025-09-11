def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()

def forward():
    if wall_in_front():
        turn_left()
    elif wall_on_right():
         move()
    else:
        turn_right()
            
def start():
    put()
    move()

start()
while not object_here():
    forward()

        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
