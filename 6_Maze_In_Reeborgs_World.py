# day 6 - Reeborg's Maze!

import random

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if(wall_in_front() and not right_is_clear()):
        turn_left()
    elif (right_is_clear()):
        turn_right()
        move()
    elif (wall_in_front()):
        turn_right()
    else:
        move()