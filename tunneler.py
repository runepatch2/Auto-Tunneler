import minescript
import time

# Gets the cardinal direction the player is facing. Does this by taking modulus of yaw with 360 to get value between 0 and 360
def getDirection():
    yaw, pitch = list(minescript.player_orientation())
    yaw = yaw % 360
    print(f"Current orientation {yaw, pitch}")
    direction = ""
    if yaw == 0.0: return "S"
    if (135 < yaw < 225): direction = "N"
    elif (225 < yaw < 315): direction = "E"
    elif (0 < yaw < 45) or (315 < yaw < 360): direction = "S"
    else: direction = "W"
    # This is needed to know what direction to make player face
    return direction

def getDistance():
    return minescript.player_get_targeted_block().distance

def faceForward(direction):
    print(direction)
    if direction == "N": minescript.player_set_orientation(180, 0)
    if direction == "E": minescript.player_set_orientation(270, 0)
    if direction == "W": minescript.player_set_orientation(90, 0)
    if direction == "S": minescript.player_set_orientation(0, 0)

def hugBlock():
    distance = minescript.player_get_targeted_block().distance
    while (distance > 1.8):
        distance = minescript.player_get_targeted_block().distance
        print(distance)
        minescript.player_press_forward(True)
    minescript.player_press_forward(False)

def mineBlocks():
    topBroken = False
    bottomBroken = False
    distance = getDistance()
    while not topBroken:
        distance = getDistance()
        if distance < 1.8:
            minescript.player_press_attack(True)
        else: 
            minescript.player_press_attack(False)
            topBroken = True
    yaw, pitch = list(minescript.player_orientation())
    print("TOP BROKEN")
    minescript.player_set_orientation(yaw, pitch + 35)
    time.sleep(0.2)

    side = minescript.player_get_targeted_block().side

    while (side == "up"):
        side = minescript.player_get_targeted_block().side
        minescript.player_press_attack(True)
    minescript.player_press_attack(False)
    print("BOTTOM BROKEN")



    

# Once block is broken (distance detected), face down by 35 degrees

while True:
    direction = getDirection()
    faceForward(direction)
    hugBlock()
    mineBlocks()