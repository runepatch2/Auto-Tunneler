import random
import sys

# Need to take the number of dice, and for each one, roll a random number between 1 and the number of sides.

def dice_roll(num_dice: int, sides: int):
    for i in range(1, num_dice + 1):
        roll = random.randint(1, sides)
        print(f"Dice #{i} rolled a {roll}")


try:
    num_dice = sys.argv[1]
    sides = sys.argv[2]
except IndexError:
    num_dice = 1
    sides = 6
    print("Invalid arguments! Defaulting to 1 die and 6 sides")

print(f"Now rolling {num_dice} {sides}-sided dice")

dice_roll(int(num_dice), int(sides))