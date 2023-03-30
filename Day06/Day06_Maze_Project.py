def turn_right():
    turn_left()
    turn_left()
    turn_left()
count = 0    
while at_goal() == False:
    while wall_on_right() == False:
        turn_right()
        move()
        count = count + 1
        if count > 30 and front_is_clear() == True:
            move()
            count = 0
            break

    while wall_on_right() == True:
        if wall_in_front() == True:
            turn_left()
        else:
            move()
    