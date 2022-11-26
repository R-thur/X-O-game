# def display(row1, row2, row3):
#     print(row1)
#     print(row2)
#     print(row3)
#
#
# row1 = [' ', ' ', ' ']
# row2 = [' ', ' ', ' ']
# row3 = [' ', ' ', ' ']
#
#
# def user_choice():
#     # Initial
#     choice = 'WRONG'
#     acceptable_range = range(1, 10)
#     within_range = False
#
#     # Two conditions to check
#     while choice.isdigit() == False or within_range == False:
#
#         choice = input('Enter a number 1-9:')
#
#         # Digit check
#         if choice.isdigit() == False:
#             print('Sorry that is not a digit')
#
#         # Range check
#         if choice.isdigit() == True:
#             if int(choice) in acceptable_range:
#                 within_range = True
#             else:
#                 print('Sorry, you are out of acceptable range')
#                 within_range = False
#
#     return int(choice)
# import random

################### GAME #############################

# def display_game(gamelist):
#     print('Here is the current list')
#     print(gamelist)
#
#
# def position_choice():
#     choice = 'wrong'
#
#     while choice not in ['0', '1', '2']:
#
#         choice = input('Pick a position(0,1,2):_')
#
#         if choice not in ['0', '1', '2']:
#             print('Sorry, invalid choice')
#
#     return int(choice)
#
#
# def replacement_choice(gamelist, position):
#     user_placement = input('Type a string to place at position:_')
#
#     gamelist[position] = user_placement
#
#     return gamelist
#
#
# def gameon_choice():
#     choice = 'wrong'
#
#     while choice not in ['Y', 'N']:
#
#         choice = input('Keep playing? (Y or N)_')
#
#         if choice not in ['Y', 'N']:
#             print('Please choose Y or N')
#
#     return True if choice == 'Y' else False
#
#
# game_on = True
# game_list = [0, 1, 2]
#
# while game_on:  # game_on == True
#
#     display_game(game_list)
#
#     position = position_choice()
#
#     game_list = replacement_choice(game_list, position)
#
#     display_game(game_list)
#
#     game_on = gameon_choice()


def display(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
    print('____________')


def pop_push_display(digit, xo):
    game_board.pop(digit - 1)
    game_board.insert(digit - 1, xo)

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

    if game_board[0] == xo and game_board[1] == xo and game_board[2] == xo \
            and winner == False:
        game_on = False
        winner = True
        print(f'{player} wins!')

    if game_board[3] == xo and game_board[4] == xo and game_board[5] == xo \
            and winner == False:
        game_on = False
        winner = True
        print(f'{player} wins!')

    if game_board[6] == xo and game_board[7] == xo and game_board[8] == xo \
            and winner == False:
        game_on = False
        winner = True
        print(f'{player} wins!')

    if game_board[0] == xo and game_board[3] == xo and game_board[6] == xo \
            and winner == False:
        game_on = False
        winner = True
        print(f'{player} wins!')

    if game_board[1] == xo and game_board[4] == xo and game_board[7] == xo \
            and winner == False:
        game_on = False
        winner = True
        print(f'{player} wins!')

    if game_board[2] == xo and game_board[5] == xo and game_board[8] == xo \
            and winner == False:
        game_on = False
        winner = True
        print(f'{player} wins!')

    if game_board[0] == xo and game_board[4] == xo and game_board[8] == xo \
            and winner == False:
        game_on = False
        winner = True
        print(f'{player} wins!')

    if game_board[2] == xo and game_board[4] == xo and game_board[6] == xo \
            and winner == False:
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


game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
fr_cells = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
game_on = True

init()
