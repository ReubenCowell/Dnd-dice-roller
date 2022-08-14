from random import randint  # random numbers are used to create a die roll


def dice_roll(dice, sides, modifier):  # returns a list of rolled dice and the sum of that list
    rolled = []
    for _ in range(0, dice):
        rolled.append(randint(1, int(sides)))
    return rolled, sum(rolled) + int(modifier)  # returns a list of the rolled dice and the total of them


def get_values(die):
    global d_num, d_sides, m
    d_loc = die.find("d")  # this gets where the character d is in the string
    if d_loc == -1:
        raise ValueError("No d found")
    d_num = int(die[:d_loc])  # gets the number of dice
    die = die[d_loc + 1:]  # removes the number of dice from the rest of the string

    if die.find("+") != -1:
        m = die[die.find("+"):]
        d_sides = die[:die.find("+")]
    elif die.find("-") != -1:
        m = die[die.find("-"):]
        d_sides = die[:die.find("-")]
    else:
        d_sides = int(die)
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
        print(str(output[1]) + ": " + string)
    except ValueError:
        print("Dice entered incorrectly")
