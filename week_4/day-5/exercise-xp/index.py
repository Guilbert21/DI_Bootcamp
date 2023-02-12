board = [[' ' for x in range(3)] for y in range(3)]
players = ['X', 'O']
turn = 0

def print_board():
    print('---+---+---')
    for row in board:
        print(' {} | {} | {} '.format(*row))
        print('---+---+---')

def check_win():
    for player in players:
        for row in range(3):
            if all(square == player for square in board[row]):
                return player
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return player
        if all(board[i][i] == player for i in range(3)):
            return player
        if all(board[i][2-i] == player for i in range(3)):
            return player
    return None

def play_game():
    global turn
    while True:
        print_board()
        row = int(input("Player {}: Choose a row (0, 1, 2): ".format(players[turn % 2])))
        col = int(input("Player {}: Choose a column (0, 1, 2): ".format(players[turn % 2])))
        if board[row][col] == ' ':
            board[row][col] = players[turn % 2]
            turn += 1
            winner = check_win()
            if winner:
                print_board()
                print("Player {} wins!".format(winner))
                break
            if turn == 9:
                print_board()
                print("Tie game.")
                break
        else:
            print("Square already occupied.")

if __name__ == '__main__':
    play_game()


