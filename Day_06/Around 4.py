def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def forward():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
            
def start():
    put()
    while not front_is_clear():
        turn_left()
    move()
    
start()
while not object_here():
    forward()

        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
