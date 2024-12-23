def draw_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[i*3], '|', board[i*3+1], '|', board[i*3+2], '|')
        print('-------------')

def check_win(board, player):
    # Sprawdzamy wiersze, kolumny i przekątne
    for i in range(3):
        if all(board[i*3+j] == player for j in range(3)) or \
           all(board[i+j*3] == player for j in range(3)):
            return True
    if all(board[i*4] == player for i in range(3)) or \
       all(board[i*2+2] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for cell in board)

def play_game():
    board = [' '] * 9
    current_player = 'X'

    while True:
        draw_board(board)
        move = int(input(f"Ruch gracza {current_player}: ")) - 1

        if board[move] == ' ':
            board[move] = current_player
            if check_win(board, current_player):
                draw_board(board)
                print(f"Wygrał gracz {current_player}!")
                break
            elif is_board_full(board):
                draw_board(board)
                print("Remis!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("To pole jest już zajęte!")

play_game()
