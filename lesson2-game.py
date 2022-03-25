
from tkinter import END


lmap1 = [
    [0,12,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [1,0,0,24]
        ]
lmap2 = [
    [0,1,1,1,0,0],
    [0,0,0,1,0,0],
    [1,1,12,1,0,0],
    [0,1,0,1,0,0],
    [0,1,0,0,24,0],
    [0,1,0,0,1,0]
        ]
map = lmap2
startposX = 0
startposY = 0
def search_start(sX, sY):
    y = 0
    x = 0
    while y < len(map):
        while x < len(map):
            if map[y][x] == 12:
                sX = x
                sY = y
                return(sX, sY)
            x += 1
        y += 1    
    print("Start is at: X ", x)
    print("Start is at: Y ", y)
    
startpos = search_start(0,0)
startposX = startpos[0]
startposY = startpos[1]
playerposX = startposX
playerposY = startposY
def move(step, playerposX, playerposY, finished = False):
    print("current step: ", step)
    print("Current position X:", playerposX)
    print("Current position Y:", playerposY)
    can_move_right = playerposX <= 2 and map[playerposY][playerposX+1] == 0
    can_move_left = playerposX >= 0 and map[playerposY][playerposX-1] == 0
    can_move_down = playerposY <= 2 and map[playerposY+1][playerposX] == 0
    can_move_up = playerposY >= 0 and map[playerposY-1][playerposX] == 0
    finish_R = playerposX <= 2 and map[playerposY][playerposX+1] == 24
    finish_D = playerposY <= 2 and map[playerposY+1][playerposX] == 24    
    finished = map[playerposY][playerposX] == 24
        
    if finish_R:
        print("The finish is on the right! -->")
        return[playerposX+1, playerposY, finished]
    if finish_D:
        print("The finish is below! \/")
        return[playerposX, playerposY+1, finished]

    if can_move_right:
        print("Going right -->")
        return[playerposX+1, playerposY, finished]
    if can_move_down:
        print("Going down \/")
        return[playerposX, playerposY+1, finished]
    if finished:
        print("Finish!")
        return[playerposX, playerposY, finished]
    return [playerposX, playerposY, finished]

current_step = 1
ttl = 10
newpos = move(current_step, startposX, startposY)
while newpos or current_step << ttl:
    current_step += 1
    newpos = move(current_step, newpos[0], newpos[1])
    finished = newpos[2]
    if finished:
        break
    if current_step >= ttl:
        break
print("Finished!")