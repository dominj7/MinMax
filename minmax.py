
from math import inf


def is_available(grid, row, column):
    return grid[row][column] == 0


def is_winner(grid, player):
    for i in range(3):
        if grid[i][0] == player and grid[i][1] == player and grid[i][2] == player:
            return True
        if grid[0][i] == player and grid[1][i] == player and grid[2][i] == player:
            return True
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    if grid[2][0] == player and grid[1][1] == player and grid[0][2] == player:
        return True
    return False


def is_full(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return False
    return True


def minmax(grid, is_maximizing):
    if is_winner(grid, 1):
        return -1
    if is_winner(grid, 2):
        return 1
    if is_full(grid):
        return 0

    if is_maximizing:
        best = -inf
        for row in range(3):
            for col in range(3):
                if is_available(grid, row, col):
                    grid[row][col] = 2
                    best = max(best, minmax(grid, False))
                    grid[row][col] = 0
        return best

    if not is_maximizing:
        best = inf
        for row in range(3):
            for col in range(3):
                if is_available(grid, row, col):
                    grid[row][col] = 1
                    best = min(best, minmax(grid, True))
                    grid[row][col] = 0
        return best


def get_move(grid):
    best = -inf
    move = ()
    for row in range(3):
        for col in range(3):
            if is_available(grid, row, col):
                grid[row][col] = 2
                score = minmax(grid, False)
                grid[row][col] = 0
                if score > best:
                    best = score
                    move = (row, col)
    return move
