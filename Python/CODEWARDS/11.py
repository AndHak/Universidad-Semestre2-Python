"""
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's
current state is solved, wouldn't we? Our goal is to create
a function that will check that for us!

Assume that the board comes in the form of a 3x3 array
where the value is 0 if a spot is empty, 1 if it is an
"X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
We want our function to return:

-1 if the board is not yet finished AND no one has won yet (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
"""

def is_solved(board):
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return -1

    return 0
            

board = [[2, 2, 1],
         [1, 1, 1],
         [2, 1, 2]]

print(is_solved(board))
            