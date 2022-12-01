def display(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('____________')


def pop_push_display(digit, xo):
    game_board[digit] = xo
    fr_cells_key = list(fr_cells.keys())[list(fr_cells.values()).index(digit)]

    fr_cells.pop(fr_cells_key)

    display(game_board)


def ai_think():
    import random
    string, number = random.choice(list(fr_cells.items()))

    return number


def choose_cell():
    choice = 'wrong'

    while choice not in fr_cells:
        choice = input('Choose a cell:_')

        if choice not in fr_cells:
            print('Sorry, invalid choice')

    return int(choice)


def check_winner(xo, player):
    global game_on
    winner = False

    if game_board[1] == game_board[2] == game_board[3] == xo or \
            game_board[4] == game_board[5] == game_board[6] == xo or \
            game_board[7] == game_board[8] == game_board[9] == xo or \
            game_board[1] == game_board[4] == game_board[7] == xo or \
            game_board[2] == game_board[5] == game_board[8] == xo or \
            game_board[3] == game_board[6] == game_board[9] == xo or \
            game_board[1] == game_board[5] == game_board[9] == xo or \
            game_board[3] == game_board[5] == game_board[7] == xo and \
            winner == False:
        game_on = False
        winner = True
        print(f'{player} wins!')

    if len(fr_cells) == 0 and winner == False:
        game_on = False
        print(f'TIE!')


def tip():
    print('|1|2|3|')
    print('|4|5|6|')
    print('|7|8|9|')


def init():
    print('Welcome to X-0')
    tip()

    while game_on:
        player_choice = choose_cell()
        pop_push_display(player_choice, 'X')
        check_winner('X', 'Player')

        if game_on:
            ai_choice = ai_think()
            pop_push_display(ai_choice, 'O')
            check_winner('O', 'Computer')


game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
fr_cells = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
game_on = True

init()
