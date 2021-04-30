'''
@Author: Vishal Salaskar
@Date: 2021-02-30
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-30 
@Title : To play a tictactoe
'''
# To create a 9 position for board position
boardpos={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
"""
Description:
A printBorad  function is created to print the board after taking input
Parameter:
board is the input printed in printBoard function
"""

def player(boardpos, turn, i):
    try:
        print('Player ' + turn + ', Enter your postion number between 1-9 ')
    except ValueError:
        print("Enter a correct position")

    turn1 = int(input())
    if boardpos[turn1] == ' ':
        boardpos[turn1] = turn
        printBoard(boardpos)

    else:
        print('Postion is played. Play again.:')
        player(boardpos, turn, i)

    if (i >= 4):

        if (boardpos[1] == boardpos[2] == boardpos[3] == turn or boardpos[4] == boardpos[5] == boardpos[6] == turn or boardpos[7] == boardpos[8] ==
                boardpos[9] == turn or boardpos[1] == boardpos[4] == boardpos[7] == turn or boardpos[2] == boardpos[5] == boardpos[8] == turn or
                boardpos[3] == boardpos[6] == boardpos[9] == turn or boardpos[1] == boardpos[5] == boardpos[9] == turn or boardpos[3] == boardpos[5] ==
                boardpos[7] == turn):
            printBoard(boardpos)
            print(turn + ' WON')
            return 1
"""
Description:
player function to take input position of player and then check if the player won using if 
Parameter:
boardpos is the board position 
"""


def tictactoe():
    turn = 'o'
    try:
        for i in range(10):
            if i == 9:
                print("Game tied")
                break
            if (player(boardpos, turn, i) == 1):
                break
            if (turn == 'x'):
                turn = 'o'
            else:
                turn = 'x'
        print("Played Well")
    except NameError as e:
        print(e)    
"""
Description:
A tictactoe function using if else to check if game tied or exit if player won and change turns of player
"""
tictactoe()