
import pygame as pg
from sys import exit
from numpy import zeros
from minmax import get_move, is_available

# Constant
WIDTH = 900
HEIGHT = 900
BACKGROUND_COLOR = (98, 114, 164)
GRID_COLOR = (68, 71, 90)
CIRCLE_COLOR = (182, 185, 200)
CROSS_COLOR = (55, 57, 73)
LINE_WIDTH = 15
RADIUS = 100
SPACE_SIZE = 300

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Tic Tac Toe')
screen.fill(BACKGROUND_COLOR)
# icon = pg.image.load("icon.png")
# pg.display.set_icon(icon)

# Drawing grid
pg.draw.line(screen, GRID_COLOR, (0, SPACE_SIZE), (3 * SPACE_SIZE, SPACE_SIZE), LINE_WIDTH)
pg.draw.line(screen, GRID_COLOR, (0, 2 * SPACE_SIZE), (3 * SPACE_SIZE, 2 * SPACE_SIZE), LINE_WIDTH)
pg.draw.line(screen, GRID_COLOR, (SPACE_SIZE, 0), (SPACE_SIZE, 3 * SPACE_SIZE), LINE_WIDTH)
pg.draw.line(screen, GRID_COLOR, (2 * SPACE_SIZE, 0), (2 * SPACE_SIZE, 3 * SPACE_SIZE), LINE_WIDTH)

grid = zeros((3, 3))


def draw_figure(row, column, player):
    grid[row][column] = player
    if player == 1:     # Circle
        center = (int(column * SPACE_SIZE + SPACE_SIZE / 2), int(row * SPACE_SIZE + SPACE_SIZE / 2))
        pg.draw.circle(screen, CIRCLE_COLOR, center, RADIUS, LINE_WIDTH)
    else:               # Cross
        top_left = (column * SPACE_SIZE + 50, row * SPACE_SIZE + 50)
        bottom_right = (column * SPACE_SIZE + SPACE_SIZE - 50, int(row * SPACE_SIZE + SPACE_SIZE - 50))
        pg.draw.line(screen, CROSS_COLOR, top_left, bottom_right, 20)
        bottom_left = (column * SPACE_SIZE + 50, row * SPACE_SIZE + SPACE_SIZE - 50)
        top_right = (column * SPACE_SIZE + SPACE_SIZE - 50, int(row * SPACE_SIZE + 50))
        pg.draw.line(screen, CROSS_COLOR, bottom_left, top_right, 20)


def draw_winning_line(row, col):
    if col is None:     # vertical line
        pg.draw.line(screen, GRID_COLOR, (20, row * SPACE_SIZE + SPACE_SIZE / 2), (3 * SPACE_SIZE - 20, row * SPACE_SIZE + SPACE_SIZE / 2), LINE_WIDTH)
    elif row is None:   # horizontal line
        pg.draw.line(screen, GRID_COLOR, (col * SPACE_SIZE + SPACE_SIZE / 2, 20), (col * SPACE_SIZE + SPACE_SIZE / 2, 3 * SPACE_SIZE - 20), LINE_WIDTH)
    else:
        if row == 0:
            start_end = (50, 3 * SPACE_SIZE - 50)
        else:
            start_end = (3 * SPACE_SIZE - 50, 50)
        pg.draw.line(screen, GRID_COLOR, (50, start_end[0]), (3 * SPACE_SIZE - 50, start_end[1]), 20)


def check_win(player):
    for i in range(3):
        if grid[i][0] == player and grid[i][1] == player and grid[i][2] == player:
            draw_winning_line(i, None)
            return True
        if grid[0][i] == player and grid[1][i] == player and grid[2][i] == player:
            draw_winning_line(None, i)
            return True
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        draw_winning_line(0, 0)
        return True
    if grid[2][0] == player and grid[1][1] == player and grid[0][2] == player:
        draw_winning_line(2, 0)
        return True
    return False


def game_over():
    if check_win(1) or check_win(2):
        return True
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return False
    return True


your_turn = True
# Game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if not your_turn and not game_over():
            choice = get_move(grid)
            draw_figure(choice[0], choice[1], 2)
            game_over()
            your_turn = True
        if event.type == pg.MOUSEBUTTONDOWN and your_turn and not game_over():
            clicked_column = int(event.pos[0] / SPACE_SIZE)
            clicked_row = int(event.pos[1] / SPACE_SIZE)
            if is_available(grid, clicked_row, clicked_column):
                draw_figure(clicked_row, clicked_column, 1)
                game_over()
                your_turn = False

    pg.display.update()
