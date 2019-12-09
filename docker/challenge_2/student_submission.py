import copy
import random

def run(player1, player2):

    """
    Your code goes between the two comment blocks.
    Do not edit anything outside of this section.
    As shown above you will recieve two variables.
    The variables are plyaer1, and player2. Each
    of these will contain one of the following
    strings:
    Grass
    Rock
    Ice
    Dragon
    Dark
    Psychic
    Bug
    Flying
    Steel
    Fire
    Fighting
    Ground
    Ghost
    Poison
    Water
    Fairy
    Electric
    Normal
    Your job is to decide if player1 or player2
    wins.
    You can go to this URL to find a chart showing
    which beats which:
    https://attackofthefanboy.com/wp-content/uploads/2016/07/Pokemon-Go-Type-Chart-633x428.jpg
    The left column beats the middle column, which beats
    the right column.
    For example if player1 conatains Flying and player2
    contains Electric, player2 wins.
    In the event that one player choses something
    that is not listed as better than the other
    player, it is a tie.
    For example if player1 contains Dragon
    and player2 contains Fire, it's a tie
    as according to the chard Fire does not
    beat dragon, nor does dragon beat fire.
    Finally if both players choose the
    same it is a tie.
    At the end of your code you should have
    a variable called result that contains
    the number 1 if player 1 wins, the number
    2 if player 2 wins, or the number 3, if a
    tie occurs.
    """

    #Your code goes here

    result = 0 #At the end of your code, this variable should be updated to either 1, 2, or 3

    """
    Do not code past this point.
    """


    return result

if __name__== "__main__":
    types = [
        'Grass',
        'Rock',
        'Ice',
        'Dragon',
        'Dark',
        'Psychic',
        'Bug',
        'Flying',
        'Steel',
        'Fire',
        'Fighting',
        'Ground',
        'Ghost',
        'Poison',
        'Water',
        'Fairy',
        'Electric',
        'Normal'
    ]

    player1 = random.choice(types)
    player2 = random.choice(types)

    print("Player1 chose: " + player1)
    print("Player2 chose: " + player2)

    print("You returned: " + str(run(player1, player2)))
