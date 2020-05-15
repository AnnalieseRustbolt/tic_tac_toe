from time import sleep


# main function
def ticTacToe():
    turns = 0

    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    pretty(board)

    while turns < 9:
        player = 'player1'

        if turns % 2 == 1:
            player = 'player2'

        print(f'{player} turn')

        board_input = input('Please type in your symbol X or O: ')
        board_input = board_input.upper()
        try:

            row = int(input('What is the row position: '))
            col = int(input('What is the col position: '))

        except:
            print('Invalid Input')

        if check_input(row, col, board_input) == True:
            # Clear screen
            print('\x1bc')
            # calls validation function

        if board[row][col] == '-':

            board[row][col] = board_input
            pretty(board)

            if check_win_row(row, board):
                # checks for complete rows
                winner = f'{player} has won'
                return winner

            elif check_win_col(col, board):
                # checks for complete columns
                winner = f'{player} has won'
                return winner

            elif check_win_diagonal(board, board_input):
                # checks for complete diagonals
                winner = f'{player} has won'
                return winner

            turns += 1

        else:
            print('That cell is occupied, please pick another')

    winner = 'The game is a draw'
    return winner


# function for input validation

def check_input(row, col, board_input):
    if row not in [0, 1, 2]:
        print('The range is from 0 - 2,choose again ')
        return False

    elif col not in [0, 1, 2]:
        print('The range is from 0 - 2,choose again ')
        return False

    elif board_input != 'X' and board_input != 'O':
        print('Invalid symbol, print either X or Y')
        return False

    else:
        return True


# function for checking for complete rows
def check_win_row(row, board):
    if board[row][0] == board[row][1] == board[row][2]:
        return True

    else:
        return False


# function for checking for complete columns
def check_win_col(col, board):
    if board[0][col] == board[1][col] == board[2][col]:
        return True

    else:
        return False


# function for checking for complete diagonals
def check_win_diagonal(board, board_input):
    if board[0][0] == board[1][1] == board[2][2] == board_input or board[2][0] == board[1][1] == board[0][
        2] == board_input:
        return True

    else:
        return False


def pretty(board):
    print(f"""

	0	{board[0][0]} \u2503 {board[0][1]} \u2503 {board[0][2]}
		\u2501\u2501\u254b\u2501\u2501\u2501\u254b\u2501\u2501
	1	{board[1][0]} \u2503 {board[1][1]} \u2503 {board[1][2]}
		\u2501\u2501\u254b\u2501\u2501\u2501\u254b\u2501\u2501
	2	{board[2][0]} \u2503 {board[2][1]} \u2503 {board[2][2]}

		0   1   2
		""")


def start():
    print("""
▀▀█▀▀ ▀█▀ ░█▀▀█ 
─░█── ░█─ ░█─── 
─░█── ▄█▄ ░█▄▄█ """)
    sleep(0.5)
    print('\x1bc')
    print("""
▀▀█▀▀ █▀▀█ █▀▀ 
░░█░░ █▄▄█ █░░ 
░░▀░░ ▀░░▀ ▀▀▀ """)
    sleep(0.5)
    print('\x1bc')
    print("""
▀▀█▀▀ █▀▀█ █▀▀ 
░░█░░ █░░█ █▀▀ 
░░▀░░ ▀▀▀▀ ▀▀▀ """)
    sleep(0.5)
    print('\x1bc')

    print(ticTacToe())


start()




