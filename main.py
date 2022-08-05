from random import randint
import re


def dice_roll(sides, dice):  # returns a list of rolled dice and the sum of that list
    rolled = []
    for _ in range(0, dice):
        rolled.append(randint(1, int(sides)))
    #    total = sum(rolled)
    return rolled, sum(rolled)


dice = input("Please input dice to be rolled")
# splitted= dicerequested[1:].split('+')
# num_of_dice = dicerequested[:1]

# sides_on_dice = int(splitted[0].split('+')[0]
# print(dice_roll(num_of_dice, sides_on_dice))

num_dice = dice[:1]
dice = dice[1:]

if '+' in dice:
    dice = dice.split('+')
    modifier = dice[1]
    sides_dice = dice[0]
elif '-' in dice:
    dice = dice.split('-')
    modifier = dice[1]
    sides_dice = dice[0]
else:
    sides_dice = dice[1:]

print(num_dice, sides_dice)
