from random import randint  # random numbers are used to create a dice roll


def dice_roll(dice, sides, modifier):  # returns a list of rolled dice and the sum of that list
    rolled = []
    for _ in range(0, dice):
        rolled.append(randint(1, int(sides)))
    return rolled, sum(rolled) + int(modifier) # returns a list of the rolled dice and the total of them


def get_values(dice):
    global d_num, d_sides, m
    d_loc = dice.find("d")  # this gets where the character d is in the string
    if d_loc == -1:
        raise ValueError("No d found")
    d_num = int(dice[:d_loc])  # gets the number of dice
    dice = dice[d_loc + 1:]  # removes the number of dice from the rest of the string

    if dice.find("+") != -1:
        m = dice[dice.find("+"):]
        d_sides = dice[:dice.find("+")]
    elif dice.find("-") != -1:
        m = dice[dice.find("-"):]
        d_sides = dice[:dice.find("-")]
    else:
        d_sides = int(dice)
        m = 0


while True:
    try:
        dice = str(input(
            "Please input dice to be rolled \n In format ?d? +/- ?")).strip().lower()  # gets the dice that user
        # wants to roll
        if dice == "stop":
            print("Ending dice roller...")
            break
        get_values(dice)
        output = dice_roll(d_num, d_sides, m)
        string = ', '.join([str(x) for x in output[0]])
        print(str(output[1])+": "+string)
    except ValueError:
        print("Dice entered incorrectly")
