import copy
import random

def run(board, player_1_score, player_2_score):

    """
    Your code goes between the two comment blocks.
    Do not edit anything outside of this section.

    You are playing the game Mancala. Rules for
    Mancala can be found here:
    https://endlessgames.com/wp-content/uploads/Mancala_Instructions.pdf

    Each time your code runs it will be selecting
    what space to pick for one turn of the game.

    The board variable contains a two dimensional array.
    The array is 6 x 2. To access the values of the array
    you can use the variable like so:
    board[x][y]

    In the above scenrio x would be replaced with a
    number between 0 and 5. And y would be replaced
    with a number between 0 and 1

    The x value traverses the board from left to
    right across the six spaces.

    The y value chooses between your side of the
    board and your opponents. 0 is your side of the
    board. 1 is your opponents.

    The player_1_score and player_2_score variables
    containt the current score for each player.

    You are player 1.

    You must return a value between 0 and 5.

    That will abe the space you choose for your turn.

    If you select a number outside that range, you will
    forfeit your turn. You will also forfeit your turn
    if you select a space that is empty.

    """

    #Your code goes here

    choice = 0 # At the end of your code, this variable should have a number between 0 and 5 representing your choice of move

    """
    Do not code past this point.
    """


    return choice

def update_board(game_info, player, option):
    board = game_info[0]
    player_1_score = game_info[1]
    player_2_score = game_info[2]
    stones = board[option][player]
    board[option][player] = 0
    opponent = False
    if player == 1:
        opponent = True

    x = option
    while stones > 0:
        if x == 5 and opponent == False:
            x = x + 1
            player_1_score = player_1_score + 1
            stones = stones - 1
            opponent = True
            continue

        if x == 0 and opponent == True:
            board[0][0] = board[0][0] + 1
            stones = stones - 1
            opponent = False
            continue

        if opponent == False:
            x = x + 1
            board[x][0] = board[x][0] + 1
            stones = stones - 1
            continue

        if opponent == True:
            x = x - 1
            board[x][1] = board[x][1] + 1
            stones = stones - 1
            continue

    game_info[0] = board
    game_info[1] = player_1_score
    game_info[2] = player_2_score

    return game_info

if __name__== "__main__":

    board = []
    player_1_score = 0
    player_2_score = 0
    x = 0

    while x < 6:
        board.append([4, 4])
        x = x + 1

    print("Starting board:")
    print(board)
    x = 0
    while x < 5:
        option = run(board, player_1_score, player_2_score)
        print("You chose option: " + str(option))
        if option < 0 or option > 5:
            print("You chose an invalid option. Skipping your turn...")
            x = x + 1
            continue
        elif board[option][0] == 0:
            print("That space is already empty. Skipping your turn...")
            x = x + 1
            continue

        game_info = update_board([board,player_1_score,player_2_score], 0, option)
        board = game_info[0]
        player_1_score = game_info[1]
        player_2_score = game_info[2]
        print
        print("New board: ")
        print(board)
        print("Player one's score: " + str(player_1_score))
        print("Player two's score: " + str(player_2_score))
        x = x + 1
