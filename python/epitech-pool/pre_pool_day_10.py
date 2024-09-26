import random

def create_grid():
    grid = [['X' for _ in range(7)] for _ in range(6)]
    return grid

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

def place(grid, col, user):
    for i in range(len(grid) - 1, -1, -1):
        if grid[i][col] == 'X':
            grid[i][col] = str(user)
            return i

def verify(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    token = grid[row][col]
    
    if token == 'X':
        return False

    # Vérification colonne (haut vers bas)
    if row <= rows - 4:
        if all(grid[row + i][col] == token for i in range(4)):
            return True

    # Vérification ligne (gauche vers droite)
    if col <= cols - 4:
        if all(grid[row][col + i] == token for i in range(4)):
            return True

    # Vérification diagonale descendante (<=)
    if row <= rows - 4 and col <= cols - 4:
        if all(grid[row + i][col + i] == token for i in range(4)):
            return True

    # Vérification diagonale montante (=>)
    if row >= 3 and col <= cols - 4:
        if all(grid[row - i][col + i] == token for i in range(4)):
            return True
    
    return False

def IA_column():
   col = random.randint(0, 6)
   return col

def choose_status():
    status = int(input("Enter the mode (1 or 2): "))
    return status

def play():
    grid = create_grid()
    count = 0

    status = choose_status()

    print_grid(grid)

    if (status == 1):
        while count < 42:
            col = ask_position()

            if (count % 2 == 0):
                user = 1
            else:
                user = 2

            row = place(grid, col, user)
            count += 1

            print_grid(grid)

            verif = verify(grid, row, col)

            if (not verif):
                continue
            else:
                break
    else:
        while count < 42:
            if (count % 2 == 0):
                col = ask_position()
                user = 1
            else:
                print("L'IA joue...")
                col = MCTS_decision(grid, player=2, simulations=5000)
                user = 2

            row = place(grid, col, user)
            count += 1

            print_grid(grid)

            verif = verify(grid, row, col)

            if (not verif):
                continue
            else:
                break

    print(f"The user {user} won in {count} times!")

play()



            