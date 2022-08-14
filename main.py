from random import randint  # random numbers are used to create a dice roll


def dice_roll(sides, dice):  # returns a list of rolled dice and the sum of that list
    rolled = []
    for _ in range(0, dice):
        rolled.append(randint(1, int(sides)))
    return rolled, sum(rolled)  # returns a list of the rolled dice and the total of them


dice = input("Please input dice to be rolled \n In format ?d? +/- ?")  # gets the dice that user wants to roll

