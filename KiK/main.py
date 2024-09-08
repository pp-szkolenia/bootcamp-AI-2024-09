import numpy as np


def generate_board():
    return np.full((3, 3), ".")


def put_item_on_board(board, coordinates, mark):
    if mark not in ["x", "o"]:
        return board, False

    if coordinates[0] < 0 or coordinates[0] > 2 or coordinates[1] < 0 or coordinates[1] > 2:
        return board, False

    if board[coordinates] != ".":
        return board, False

    # ... itd.

    board[coordinates] = mark

    return board, True


def check_if_game_over(board):
    for mark in ["x", "o"]:
        if np.all(board.diagonal() == mark) or np.all(np.fliplr(board).diagonal() == mark):
            return True

        for axis in [0, 1]:
            if np.any(np.all(board == mark, axis=axis)):
                return True

    if "." not in board:
        return True

    return False
