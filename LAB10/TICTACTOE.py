# Tic-Tac-Toe using Minimax
# min max checks all the future values prior to a move ; time taken is known as branching factor

board = [" " for _ in range(9)]

def print_board():
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")


def winner(b, player):
    win_pos = [(0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6)]
    return any(b[a]==b[b1]==b[c]==player for a,b1,c in win_pos)

def is_full(b):
    return " " not in b


def minimax(b, is_max):
    if winner(b,'X'):
        return 1
    if winner(b,'O'):
        return -1
    if is_full(b):
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if b[i] == " ":
                b[i] = 'X'
                score = minimax(b, False)
                b[i] = " "
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if b[i] == " ":
                b[i] = 'O'
                score = minimax(b, True)
                b[i] = " "
                best = min(best, score)
        return best


def best_move():
    best_score = -100
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = 'X'
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move


print("You are O. Positions 1-9")

while True:
    print_board()


    pos = int(input("Enter position: ")) - 1
    if board[pos] != " ":
        print("Invalid move")
        continue
    board[pos] = 'O'

    if winner(board,'O'):
        print_board()
        print("You win!")
        break
    if is_full(board):
        print_board()
        print("Draw!")
        break


    comp = best_move()
    board[comp] = 'X'
    print("Computer chose:", comp+1)

    if winner(board,'X'):
        print_board()
        print("Computer wins!")
        break
    if is_full(board):
        print_board()
        print("Draw!")
        break