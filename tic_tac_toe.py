
grid = [ [i+j*3 for i in range(1,4)] for j in range(3)]


# for row in grid :
#     print(row)

def print_board(grid):
    for row in grid:
        print(row)

def check_winner(grid, player):

    for i in range(3):
        if grid[i][0] == player and grid[i][1] == player and grid[i][2] == player:
            return True

    for i in range(3):
        if grid[0][i] == player and grid[1][i] == player and grid[2][i] == player:
            return True

    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True

    if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True

    return False


def is_draw(grid):
    for row in grid:
        for cell in row:
            if isinstance(cell,int):
                return False 
    
    return True

def get_empty_cells(grid):
    empty = []
    for row in grid:
        for cell in row:
            if isinstance(cell,int):
                empty.append(cell)
    
    return empty

def minimax(grid,player):

    if player == 'O':
        best_score = -float("inf")
    else :
        best_score = float("inf")

    if check_winner(grid,"O"):
        return 1
    if check_winner(grid,"X"):
        return -1
    
    if is_draw(grid):
        return 0

    empty_cells = get_empty_cells(grid)
    for move in empty_cells:
        for i in range(3):
            for j in range(3):
                if grid[i][j] == move:
                    grid[i][j] = player
                    if player=="O":
                        other_player="X"
                    else :
                        other_player="O"
                    score = minimax(grid,other_player)
                    grid[i][j] = move

                    if player == 'O':
                        best_score = max(best_score,score)
                    else :
                        best_score = min(best_score,score)

    return best_score


def optimal_decision(grid):
    best_score = -float("inf")
    best_move = None
    empty_cells = get_empty_cells(grid)
    
    for move in empty_cells:
        for i in range(3):
            for j in range(3):
                if grid[i][j] == move:
                    grid[i][j] = 'O'
                    score = minimax(grid,"X")
                    grid[i][j] = move
                    if score>best_score:
                        best_score = score 
                        best_move = move
    

    return best_move




while True :
    move = int(input("Enter your move"))
    valid = False
    for i in range(3) :
        for j in range(3):
            if move == grid[i][j]:
                grid[i][j]="X"
                valid = True
    print(f'User Moves ... \n')
    print_board(grid)
    if not valid :
        print("Move is not valid !!")
        continue

    if check_winner(grid,"X"):
        print("X(Player Wins)")
        break
    
    print("AI moves ....")

    ai_move = optimal_decision(grid)

    for i in range(3):
        for j in range(3):
            if grid[i][j] == ai_move:
                grid[i][j] = 'O'
                break
        else:
            continue
        break

    print_board(grid)
    

    if check_winner(grid,"O"):
        print("O(Machine Wins)")
        break
    
    if is_draw(grid):
        print('Draw')
        break

