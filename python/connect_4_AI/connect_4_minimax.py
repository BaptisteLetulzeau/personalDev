import math
import random
import copy

def minimax(grid, depth, alpha, beta, maximizingPlayer):
    valid_moves = get_valid_moves(grid)
    is_last = is_last_node(grid)

    # Évaluation si le nœud est terminal ou si la profondeur est atteinte
    if depth == 0 or is_last:
        if is_last:
            if verify_grid(grid, 2):
                return (None, 100000000000000)  # Grande valeur positive si l'IA gagne
            elif verify_grid(grid, 1):
                return (None, -10000000000000)  # Grande valeur négative si l'adversaire gagne
            else:  # Match nul
                return (None, 0)
        else:  # Profondeur atteinte, retourner la fonction d'évaluation
            return (None, score_position(grid, 2))

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

def get_valid_moves(grid):
    return [col for col in range(7) if grid[0][col] == 'X']

def get_next_open_row(grid, col):
    for r in range(5, -1, -1):
        if grid[r][col] == 'X':
            return r

def score_position(grid, player):
    score = 0

    # Score des lignes
    for row in grid:
        row_array = [int(cell) if cell != 'X' else 0 for cell in row]
        for col in range(4):
            window = row_array[col:col + 4]
            score += evaluate_window(window, player)

    # Score des colonnes
    for col in range(7):
        col_array = [int(grid[row][col]) if grid[row][col] != 'X' else 0 for row in range(6)]
        for row in range(3):
            window = col_array[row:row + 4]
            score += evaluate_window(window, player)

    # Score diagonales ascendantes
    for row in range(3):
        for col in range(4):
            window = [int(grid[row + i][col + i]) if grid[row + i][col + i] != 'X' else 0 for i in range(4)]
            score += evaluate_window(window, player)

    # Score diagonales descendantes
    for row in range(3, 6):
        for col in range(4):
            window = [int(grid[row - i][col + i]) if grid[row - i][col + i] != 'X' else 0 for i in range(4)]
            score += evaluate_window(window, player)

    return score

def evaluate_window(window, player):
    score = 0
    opponent = 1 if player == 2 else 2

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opponent) == 3 and window.count(0) == 1:
        score -= 4

    return score

def verify_grid(grid, player):
    # rows
    for row in range(6):
        for col in range(4):
            if all(grid[row][col + i] == str(player) for i in range(4)):
                return True

    # columns
    for col in range(7):
        for row in range(3):
            if all(grid[row + i][col] == str(player) for i in range(4)):
                return True

    # up diagonal
    for row in range(3, 6):
        for col in range(4):
            if all(grid[row - i][col + i] == str(player) for i in range(4)):
                return True

    # down diagonal
    for row in range(3):
        for col in range(4):
            if all(grid[row + i][col + i] == str(player) for i in range(4)):
                return True

    return False

def is_last_node(grid):
    return verify_grid(grid, 1) or verify_grid(grid, 2) or len(get_valid_moves(grid)) == 0

def place(grid, col, player):
    row = get_next_open_row(grid, col)
    grid[row][col] = str(player)
    return row

def IA_move(grid, depth=4):
    col, minimax_score = minimax(grid, depth, -math.inf, math.inf, True)
    return col

def create_grid():
    return [['X' for _ in range(7)] for _ in range(6)]

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def ask_position():
    while True:
        user_input = input("Enter a number of column between 0 and 6: ")
        if user_input.isdigit():
            col = int(user_input)
            if 0 <= col <= 6:
                return col
            else:
                print("The number must be between 0 and 6. Try again.")
        else:
            print("Invalid input. Please enter a valid integer.")

def choose_status():
    status = int(input("Enter the mode (1 or 2): "))
    return status

def play():
    grid = create_grid()
    count = 0
    status = choose_status()

    print_grid(grid)

    if status == 1:
        while count < 42:
            col = ask_position()
            user = 1 if count % 2 == 0 else 2
            row = place(grid, col, user)
            count += 1
            print_grid(grid)
            if verify_grid(grid, int(grid[row][col])):
                break
    else:
        while count < 42:
            if count % 2 == 0:
                col = ask_position()
                user = 1
            else:
                print("L'IA joue...")
                col = IA_move(grid, depth=4)
                user = 2
            row = place(grid, col, user)
            count += 1
            print_grid(grid)
            if verify_grid(grid, int(grid[row][col])):
                break

    print(f"The user {user} won in {count} moves!")

play()
