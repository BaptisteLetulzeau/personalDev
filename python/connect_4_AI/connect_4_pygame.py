import math
import random
import copy
import pygame
import sys

# constants
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
WIDTH = 7 * SQUARESIZE
HEIGHT = (6 + 1) * SQUARESIZE
SIZE = (WIDTH, HEIGHT)

# colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# init pygame
pygame.init()
screen = pygame.display.set_mode(SIZE)

def create_grid():
    """create the grid"""
    return [['X' for _ in range(7)] for _ in range(6)]

def draw_grid(grid):
    """draw the grid in pygame"""
    # draw the grid
    for row in range(6):
        for col in range(7):
            pygame.draw.rect(screen, BLUE, (col * SQUARESIZE, row * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(col * SQUARESIZE + SQUARESIZE / 2), int(row * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    # draw the pieces
    for row in range(6):
        for col in range(7):
            # player 1
            if grid[row][col] == '1':
                pygame.draw.circle(screen, RED, (int(col * SQUARESIZE + SQUARESIZE / 2), (SQUARESIZE // 2) + (row + 1) * SQUARESIZE), RADIUS)
            # IA
            elif grid[row][col] == '2':
                pygame.draw.circle(screen, YELLOW, (int(col * SQUARESIZE + SQUARESIZE / 2), (SQUARESIZE // 2) + (row + 1) * SQUARESIZE), RADIUS)

    pygame.display.update()


def get_valid_moves(grid):
    """return moves where we can play"""
    return [col for col in range(7) if grid[0][col] == 'X']

def get_next_open_row(grid, col):
    """return the first available row"""
    for row in range(6 - 1, -1, -1):
        if grid[row][col] == 'X':
            return row
    return -1

def place(grid, col, player):
    """place a piece with a column and a row"""
    row = get_next_open_row(grid, col)
    if row != -1:
        grid[row][col] = str(player)

def is_last_node(grid):
    """detect if the piece is in the last node"""
    return verify_grid(grid, 1) or verify_grid(grid, 2) or len(get_valid_moves(grid)) == 0

def verify_grid(grid, player):
    """verify if there is a winning line"""
    # lines
    for row in range(6):
        for col in range(7 - 3):
            if all(grid[row][col + i] == str(player) for i in range(4)):
                return True

    # columns
    for col in range(7):
        for row in range(6 - 3):
            if all(grid[row + i][col] == str(player) for i in range(4)):
                return True

    # up diagonals
    for row in range(3, 6):
        for col in range(7 - 3):
            if all(grid[row - i][col + i] == str(player) for i in range(4)):
                return True

    # down diagonals
    for row in range(6 - 3):
        for col in range(7 - 3):
            if all(grid[row + i][col + i] == str(player) for i in range(4)):
                return True
            
    # if not winning lines
    return False

def minimax(grid, depth, alpha, beta, maximizingPlayer):
    """determines the minimax move"""
    valid_moves = get_valid_moves(grid)
    is_last = is_last_node(grid)

    if depth == 0 or is_last:
        if is_last:
            if verify_grid(grid, 2):
                return (None, 100000000000000)
            elif verify_grid(grid, 1):
                return (None, -10000000000000)
            else:
                return (None, 0)
        else:
            # return the best score
            return (None, 0)

    # if we search for the best score
    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_moves)
        for col in valid_moves:
            temp_grid = copy.deepcopy(grid)
            place(temp_grid, col, 2)
            new_score = minimax(temp_grid, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value

    # if we want to minimalize the score of the ennemy
    else:
        value = math.inf
        best_col = random.choice(valid_moves)
        for col in valid_moves:
            temp_grid = copy.deepcopy(grid)
            place(temp_grid, col, 1)
            new_score = minimax(temp_grid, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value

def IA_move(grid, depth=4):
    """determines IA move"""
    col, minimax_score = minimax(grid, depth, -math.inf, math.inf, True)
    return col

def play():
    """main loop"""
    grid = create_grid()
    game_over = False
    has_won = False
    player = 0
    counter = 0
    pygame.display.set_caption('Connect 4')

    pygame.font.init()
    my_font = pygame.font.SysFont("monospace", 75)

    # print firstable the grid
    draw_grid(grid)

    while not game_over:
        # we wait for events (motion of the mouse or click)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # move the cursor every 100px
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))

                posx = event.pos[0]
                col = posx // SQUARESIZE
                posx_snapped = col * SQUARESIZE + SQUARESIZE // 2

                if player == 0:
                    pygame.draw.circle(screen, RED, (posx_snapped, SQUARESIZE // 2), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx_snapped, SQUARESIZE // 2), RADIUS)

            pygame.display.update()

            # at the click of the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                if player == 0:
                    # get the position at any moment
                    posx = event.pos[0]
                    col = int(posx // SQUARESIZE)
                    if col in get_valid_moves(grid):
                        place(grid, col, 1)
                        counter += 1

                        if verify_grid(grid, 1):
                            has_won = True
                        player = 1
                        draw_grid(grid)

            if player == 1:
                col = IA_move(grid)
                if col is not None:
                    place(grid, col, 2)
                    counter += 1

                    if verify_grid(grid, 2):
                        game_over = True
                    player = 0
                    draw_grid(grid)

        if game_over or counter == 42:
            # if the IA has won
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
            label = my_font.render("Game Over !", 1, (255, 255, 255))
            screen.blit(label, (40, 10))
            pygame.display.update()

            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

        elif has_won:
            # if the user has won
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
            label = my_font.render("You have won !", 1, (255, 255, 255))
            screen.blit(label, (40, 10))
            pygame.display.update()

            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

play()
