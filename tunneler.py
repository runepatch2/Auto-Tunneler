import minescript

"""
(1)
Need to do things in order:
Detect the head-level block between the two blocks that the user is looking at
Or force user to look straight ahead

-----------
Need to first detect the nearest cardinal direction that the player is facing. (Use % operator)
To detect the nearest cardinal direction player is facing, need to take modulus of yaw % 360 to get remainder.

Need to determine when player is facing south
How i determine if it's south is if the absolute yaw is between 0 and 45 or between 315 and 360
(DONE)
-----------

-----------
To look forward, use player_set_orientation() and set yaw and pitch corresponding to direction player is facing
direction is obtained from getDirection
(DONE)
-----------


"""

# Gets the cardinal direction the player is facing. Does this by taking modulus of yaw with 360 to get value between 0 and 360
def getDirection():
    yaw, pitch = list(minescript.player_orientation())
    yaw = yaw % 360
    print(f"Current orientation {yaw, pitch}")
    direction = ""
    if (135 < yaw < 225): direction = "N"
    elif (225 < yaw < 315): direction = "E"
    elif (0 < yaw < 45) or (315 < yaw < 360): direction = "S"
    else: direction = "W"
    # This is needed to know what direction to make player face
    return direction

def faceForward(direction):
    print(direction)
    if direction == "N": minescript.player_set_orientation(180, 0)
    if direction == "E": minescript.player_set_orientation(270, 0)
    if direction == "W": minescript.player_set_orientation(90, 0)
    if direction == "S": minescript.player_set_orientation(0, 0)
    

direction = getDirection()
faceForward(direction)