"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:

    """# first check for rules violation
    amount_difference = abs(sum([line.count('x') for line in board]) -
                            sum([line.count('o') for line in board]))
    if amount_difference not in range(2):
        raise ValueError("don't break the rules!")"""

    for char in 'xo':
        # horizontal winner
        if [char for line in board if line.count(char) == 3]:
            return f"{char} wins!"
        # vertical winner
        if [char for line in range(3)
           if [board[row][line] for row in range(3)].count(char) == 3]:
            return f"{char} wins!"
        # diagonal winner
        if ([board[row][line] for line, row
            in zip(range(3), range(3))].count(char) == 3 or
                [board[row][line] for line, row in
                 zip(range(3), range(2, -1, -1))].count(char) == 3):
            return f"{char} wins!"

    # unfinished case return
    if sum([line.count('-') for line in board]) > 0:
        return "unfinished!"
    # draw case return
    return "draw!"
