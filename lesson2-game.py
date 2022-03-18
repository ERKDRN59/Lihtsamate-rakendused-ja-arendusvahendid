
lmap1 = [
    [12,0,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [1,0,0,24]
        ]
lmap2 = [
    [12,1,0,0],
    [0,0,0,0],
    [1,1,0,0],
    [0,0,0,24]
        ]
map = lmap1
startposX = 0
startposY = 0
def move(step, playerposX, playerposY):
    print("current step: ", step)
    print("Current position X:", playerposX)
    print("Current position Y:", playerposY)
    playerposX = startposX
    playerposY = startposY
    can_move_right = playerposX <= 2 and map[playerposY][playerposX+1] == 0
    can_move_down = playerposY <= 2 and map[playerposY+1][playerposX] == 0
    
    
    if can_move_right:
        print("Going right")
        playerposX += 1
    if can_move_down:
        print("Going down")
        playerposY += 1
    return [playerposX, playerposY]
newpos = move(1,startposX, startposY)
newpos = move(2, newpos[0], newpos[1])