def create_grid():
    grid = [['X' for _ in range(7)] for _ in range(6)]
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def ask_position():
    col = int(input("Enter a number of column between 0 and 6: "))
    return col

def place(grid, col, user):
    for row in reversed(grid):
        if row[col] == 'X' and user == 1:
            row[col] = '1'
            break
        elif (row[col] == 'X' and user == 2):
            row[col] = '2'
            break

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

    # Vérification diagonale descendante (\)
    if row <= rows - 4 and col <= cols - 4:
        if all(grid[row + i][col + i] == token for i in range(4)):
            return True

    # Vérification diagonale montante (/)
    if row >= 3 and col <= cols - 4:
        if all(grid[row - i][col + i] == token for i in range(4)):
            return True
    
    return False


def play():
    grid = create_grid()
    compteur = 0

    print_grid(grid)

    while compteur < 42:
        col = ask_position()

        if (compteur % 2 == 0):
            place(grid, col, user=1)
            compteur += 1
        else:
            place(grid, col, user=2)
            compteur += 1

        print_grid(grid)

        verif = verify(grid, col)

        if (not verif):
            continue
        else:
            break

    print(f"La partie est terminée en {compteur}")

play()



            