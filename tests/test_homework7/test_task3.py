import pytest
from homeworks.homework7.task3 import tic_tac_toe_checker


def test_fixed_default_examples():
    """Testing that function works right
    with two default examples(second one was fixed)"""
    board = [['-', '-', 'o'],
             ['-', 'x', 'o'],
             ['x', 'o', 'x']]
    assert tic_tac_toe_checker(board) == "unfinished!"
    board = [['-', '-', 'o'],
             ['-', 'o', 'o'],
             ['x', 'x', 'x']]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_boards_with_clear_horizontal_winner():
    """Testing that function defies a
    clear horizontal winner right"""
    board = [['o', 'o', 'o'],
             ['-', 'x', '-'],
             ['x', '-', 'x']]
    assert tic_tac_toe_checker(board) == "o wins!"
    board = [['x', 'o', '-'],
             ['x', 'x', 'x'],
             ['o', 'o', '-']]
    assert tic_tac_toe_checker(board) == "x wins!"
    board = [['-', 'x', 'x'],
             ['x', '-', '-'],
             ['o', 'o', 'o']]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_boards_with_clear_vertical_winner():
    """Testing that function defies a
    clear vertical winner right"""
    board = [['x', 'o', 'o'],
             ['x', 'o', '-'],
             ['x', '-', 'x']]
    assert tic_tac_toe_checker(board) == "x wins!"
    board = [['x', 'o', '-'],
             ['x', 'o', 'x'],
             ['-', 'o', '-']]
    assert tic_tac_toe_checker(board) == "o wins!"
    board = [['-', 'x', 'x'],
             ['o', '-', 'x'],
             ['o', 'o', 'x']]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_boards_with_clear_diagonal_winner():
    """Testing that function defies a
    clear diagonal winner right"""
    board = [['x', 'o', 'o'],
             ['-', 'x', '-'],
             ['-', '-', 'x']]
    assert tic_tac_toe_checker(board) == "x wins!"
    board = [['x', 'x', 'o'],
             ['o', 'o', 'x'],
             ['o', 'x', '-']]
    assert tic_tac_toe_checker(board) == "o wins!"
    board = [['o', 'x', 'o'],
             ['x', 'o', 'x'],
             ['x', 'x', 'o']]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_boards_with_double_winner():
    """Testing that function defies a
    double winner as a winner"""
    board = [['x', 'o', 'o'],
             ['x', 'x', 'x'],
             ['x', 'o', 'o']]
    assert tic_tac_toe_checker(board) == "x wins!"
    board = [['o', 'x', 'o'],
             ['x', 'o', 'x'],
             ['o', 'x', 'o']]
    assert tic_tac_toe_checker(board) == "o wins!"
    board = [['x', 'o', 'o'],
             ['x', 'o', 'o'],
             ['x', 'x', 'x']]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_unfinished_boards():
    """Testing that function defies
    an unfinished boards"""
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    assert tic_tac_toe_checker(board) == "unfinished!"
    board = [['-', 'o', 'x'],
             ['o', 'x', '-'],
             ['-', '-', 'x']]
    assert tic_tac_toe_checker(board) == "unfinished!"
    board = [['x', 'o', 'x'],
             ['o', '-', 'o'],
             ['x', 'o', 'x']]
    assert tic_tac_toe_checker(board) == "unfinished!"


def test_draw_boards():
    """Testing that function defies
    a draw boards"""
    board = [['x', 'o', 'x'],
             ['o', 'x', 'x'],
             ['o', 'x', 'o']]
    assert tic_tac_toe_checker(board) == "draw!"
    board = [['o', 'x', 'o'],
             ['x', 'x', 'o'],
             ['x', 'o', 'x']]
    assert tic_tac_toe_checker(board) == "draw!"
    board = [['x', 'x', 'o'],
             ['o', 'o', 'x'],
             ['x', 'x', 'o']]
    assert tic_tac_toe_checker(board) == "draw!"


def test_boards_with_violated_rules():
    """Testing that function defies
    rules violation"""
    board = [['x', 'x', 'x'],
             ['x', 'x', 'x'],
             ['o', 'o', 'o']]
    with pytest.raises(ValueError, match="don't break the rules!"):
        tic_tac_toe_checker(board)
    board = [['o', '-', 'x'],
             ['o', '-', 'x'],
             ['o', '-', 'x']]
    with pytest.raises(ValueError, match="don't break the rules!"):
        tic_tac_toe_checker(board)
    board = [['x', 'x', 'x'],
             ['x', 'x', 'x'],
             ['x', 'x', 'x']]
    with pytest.raises(ValueError, match="don't break the rules!"):
        tic_tac_toe_checker(board)
    board = [['o', 'x', 'x'],
             ['x', 'o', 'x'],
             ['x', 'x', 'o']]
    with pytest.raises(ValueError, match="don't break the rules!"):
        tic_tac_toe_checker(board)
