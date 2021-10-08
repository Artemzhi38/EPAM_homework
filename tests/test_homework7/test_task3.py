import pytest

from homeworks.homework7.task3 import tic_tac_toe_checker


@pytest.mark.parametrize("board, result", [([['-', '-', 'o'],
                                             ['-', 'x', 'o'],
                                             ['x', 'o', 'x']],
                                            "unfinished!"),
                                           ([['-', '-', 'o'],
                                             ['-', 'o', 'o'],
                                             ['x', 'x', 'x']],
                                            "x wins!")])
def test_fixed_default_examples(board, result):
    """Testing that function works right
    with two default examples(second one was fixed)"""
    assert tic_tac_toe_checker(board) == result


@pytest.mark.parametrize("board, result", [([['o', 'o', 'o'],
                                             ['-', 'x', '-'],
                                             ['x', '-', 'x']],
                                            "o wins!"),
                                           ([['x', 'o', '-'],
                                             ['x', 'x', 'x'],
                                             ['o', 'o', '-']],
                                            "x wins!"),
                                           ([['-', 'x', 'x'],
                                             ['x', '-', '-'],
                                             ['o', 'o', 'o']],
                                            "o wins!")])
def test_boards_with_clear_horizontal_winner(board, result):
    """Testing that function defies a
    clear horizontal winner right"""
    assert tic_tac_toe_checker(board) == result


@pytest.mark.parametrize("board, result", [([['x', 'o', 'o'],
                                             ['x', 'o', '-'],
                                             ['x', '-', 'x']],
                                            "x wins!"),
                                           ([['x', 'o', '-'],
                                             ['x', 'o', 'x'],
                                             ['-', 'o', '-']],
                                            "o wins!"),
                                           ([['-', 'x', 'x'],
                                             ['o', '-', 'x'],
                                             ['o', 'o', 'x']],
                                            "x wins!")])
def test_boards_with_clear_vertical_winner(board, result):
    assert tic_tac_toe_checker(board) == result


@pytest.mark.parametrize("board, result", [([['x', 'o', 'o'],
                                             ['-', 'x', '-'],
                                             ['-', '-', 'x']],
                                            "x wins!"),
                                           ([['x', 'x', 'o'],
                                             ['o', 'o', 'x'],
                                             ['o', 'x', '-']],
                                            "o wins!"),
                                           ([['o', 'x', 'o'],
                                             ['x', 'o', 'x'],
                                             ['x', 'x', 'o']],
                                            "o wins!")])
def test_boards_with_clear_diagonal_winner(board, result):
    """Testing that function defies a
    clear diagonal winner right"""
    assert tic_tac_toe_checker(board) == result


@pytest.mark.parametrize("board, result", [([['x', 'o', 'o'],
                                             ['x', 'x', 'x'],
                                             ['x', 'o', 'o']],
                                            "x wins!"),
                                           ([['o', 'x', 'o'],
                                             ['x', 'o', 'x'],
                                             ['o', 'x', 'o']],
                                            "o wins!"),
                                           ([['x', 'o', 'o'],
                                             ['x', 'o', 'o'],
                                             ['x', 'x', 'x']],
                                            "x wins!")])
def test_boards_with_double_winner(board, result):
    """Testing that function defies a
    double winner as a winner"""
    assert tic_tac_toe_checker(board) == result


@pytest.mark.parametrize("board", [[['-', '-', '-'],
                                    ['-', '-', '-'],
                                    ['-', '-', '-']],
                                   [['-', 'o', 'x'],
                                    ['o', 'x', '-'],
                                    ['-', '-', 'x']],
                                   [['x', 'o', 'x'],
                                    ['o', '-', 'o'],
                                    ['x', 'o', 'x']]])
def test_unfinished_boards(board):
    """Testing that function defies
    an unfinished boards"""
    assert tic_tac_toe_checker(board) == "unfinished!"


@pytest.mark.parametrize("board", [[['x', 'o', 'x'],
                                    ['o', 'x', 'x'],
                                    ['o', 'x', 'o']],
                                   [['o', 'x', 'o'],
                                    ['x', 'x', 'o'],
                                    ['x', 'o', 'x']],
                                   [['x', 'x', 'o'],
                                    ['o', 'o', 'x'],
                                    ['x', 'x', 'o']]])
def test_draw_boards(board):
    """Testing that function defies
    a draw boards"""
    assert tic_tac_toe_checker(board) == "draw!"


'''@pytest.mark.parametrize("board", [[['x', 'x', 'x'],
                                    ['x', 'x', 'x'],
                                    ['o', 'o', 'o']],
                                   [['o', '-', 'x'],
                                    ['o', '-', 'x'],
                                    ['o', '-', 'x']],
                                   [['x', 'x', 'x'],
                                    ['x', 'x', 'x'],
                                    ['x', 'x', 'x']],
                                   [['o', 'x', 'x'],
                                    ['x', 'o', 'x'],
                                    ['x', 'x', 'o']]])
def test_boards_with_violated_rules(board):
    """Testing that function defies
    rules violation"""
    with pytest.raises(ValueError, match="don't break the rules!"):
        tic_tac_toe_checker(board)'''
