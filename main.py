from random import randint

def dice_roll(sides):
    return randint(0, int(sides))

while True:
    dicerequested = input("Please input dice to be rolled")

    print(dice_roll(dicerequested))