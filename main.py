import time

from algorithms import *


def print_board(board):
    print(' 　ａ　ｂ　ｃ　ｄ　ｅ　ｆ　ｇ　ｈ')
    row_num = 1
    for row in board:
        print(str(row_num) + ' ', end='')
        for item in row:
            print(item + ' ', end='')
        print()
        row_num += 1


def get_move_to_string(move):
    (row, col) = move
    row += 1
    row = str(row)
    if col == 0:
        return row + 'a'
    elif col == 1:
        return row + 'b'
    elif col == 2:
        return row + 'c'
    elif col == 3:
        return row + 'd'
    elif col == 4:
        return row + 'e'
    elif col == 5:
        return row + 'f'
    elif col == 6:
        return row + 'g'
    elif col == 7:
        return row + 'h'


def get_move_from_input(move_input):
    row = int(move_input[0]) - 1
    col = move_input[1]
    if col == 'a':
        return row, 0
    elif col == 'b':
        return row, 1
    elif col == 'c':
        return row, 2
    elif col == 'd':
        return row, 3
    elif col == 'e':
        return row, 4
    elif col == 'f':
        return row, 5
    elif col == 'g':
        return row, 6
    elif col == 'h':
        return row, 7


def get_winner(board):
    w_score = get_score(board, WHITE)
    b_score = get_score(board, BLACK)
    if w_score > b_score:
        return WHITE
    elif b_score > w_score:
        return BLACK
    else:
        return "TIE"


def show_results(board):
    winner = get_winner(board)

    if winner == WHITE:
        print("Wygrały białe!")
    elif winner == BLACK:
        print("Wygrały czarne!")
    else:
        print("Remis")

    print("Wynik białych: ", get_score(board, WHITE))
    print("Wynik czarnych: ", get_score(board, BLACK))


def player_vs_AI_mode(player_color, AI_depth):
    game_board, game, turn_color = initialize_game()
    while game:
        print_board(game_board)
        if turn_color == WHITE:
            if player_color == WHITE:
                player_move = input("Twój ruch (np.: 1a): ")
                move_row, move_col = get_move_from_input(player_move)
            else:
                move_row, move_col = get_best_move(game_board, WHITE, AI_depth)
                print("Gracz wykonał ruch: " + get_move_to_string((move_row, move_col)))

        else:
            if player_color == BLACK:
                player_move = input("Twój ruch (np.: 1a): ")
                move_row, move_col = get_move_from_input(player_move)
            else:
                move_row, move_col = get_best_move(game_board, BLACK, 4)
                print("Gracz wykonał ruch: " + get_move_to_string((move_row, move_col)))

        game_board = place_disk(game_board, move_row, move_col, turn_color)

        if is_game_over(game_board):
            print_board(game_board)
            show_results(game_board)
            game = False

        if not has_additional_move(game_board, turn_color):
            turn_color = get_other_color(turn_color)


def random_vs_AI_mode(random_color, AI_depth, heuristic):
    game_board, game, turn_color = initialize_game()
    turn_color = WHITE
    while game:
        # print_board(game_board)
        if turn_color == WHITE:
            if random_color == WHITE:
                move_row, move_col = get_random_move(game_board, WHITE)
            else:
                move_row, move_col = get_best_move(game_board, WHITE, AI_depth, heuristic)
        else:
            if random_color == BLACK:
                move_row, move_col = get_random_move(game_board, BLACK)
            else:
                move_row, move_col = get_best_move(game_board, BLACK, AI_depth, heuristic)

        game_board = place_disk(game_board, move_row, move_col, turn_color)

        if is_game_over(game_board):
            print_board(game_board)
            show_results(game_board)
            game = False

        if not has_additional_move(game_board, turn_color):
            turn_color = get_other_color(turn_color)


def AI_vs_AI_mode(white_depth, black_depth, white_heuristic, black_heuristic):
    game_board, game, turn_color = initialize_game()
    turn_color = WHITE
    while game:
        # print_board(game_board)
        if turn_color == WHITE:
            move_row, move_col = get_best_move(game_board, WHITE, white_depth, white_heuristic)
        else:
            move_row, move_col = get_best_move(game_board, BLACK, black_depth, black_heuristic)

        game_board = place_disk(game_board, move_row, move_col, turn_color)

        if is_game_over(game_board):
            print_board(game_board)
            show_results(game_board)
            game = False

        if not has_additional_move(game_board, turn_color):
            turn_color = get_other_color(turn_color)


def analysis_mode(random_color, AI_depth, heuristic):
    game_board, game, turn_color = initialize_game()
    turn_color = WHITE
    while game:
        # print_board(game_board)
        if turn_color == WHITE:
            if random_color == WHITE:
                move_row, move_col = get_random_move(game_board, WHITE)
            else:
                move_row, move_col = get_best_move(game_board, WHITE, AI_depth, heuristic)
        else:
            if random_color == BLACK:
                move_row, move_col = get_random_move(game_board, BLACK)
            else:
                move_row, move_col = get_best_move(game_board, BLACK, AI_depth, heuristic)

        game_board = place_disk(game_board, move_row, move_col, turn_color)

        if is_game_over(game_board):
            return get_winner(game_board)

        if not has_additional_move(game_board, turn_color):
            turn_color = get_other_color(turn_color)


if __name__ == "__main__":
    print('Tryb gry:')
    print('1. Gracz vs AI')
    print('2. Random vs AI')
    print('3. AI vs AI')
    choice = input()

    if int(choice) == 1:
        print('Wybierz kolor:')
        print('1. Białe')
        print('2. Czarne')
        choice = input()
        if int(choice) == 1:
            player_vs_AI_mode(WHITE, 5)
        else:
            player_vs_AI_mode(BLACK, 5)
    elif int(choice) == 2:
        print('Wybierz kolor gracza random:')
        print('1. Białe')
        print('2. Czarne')
        color = input()
        print('Wybierz strategie gracza AI:')
        print('1. Ważona plansza')
        print('2. Punkty, plansza, mobilnosc')
        print('3. Adaptacyjnie: punkty, plansza, mobilnosc')
        strategy = input()
        exe_start_time = time.time()
        if int(color) == 1:
            random_vs_AI_mode(WHITE, 3, int(strategy))
        else:
            random_vs_AI_mode(BLACK, 3, int(strategy))
        exe_end_time = time.time()
        print(exe_end_time - exe_start_time)
    elif int(choice) == 3:
        print('Wybierz strategie gracza AI - białe:')
        print('1. Ważona plansza')
        print('2. Punkty, plansza, mobilnosc')
        print('3. Adaptacyjnie: punkty, plansza, mobilnosc')
        white_heuristic = input()
        print('Wybierz strategie gracza AI - czanre:')
        print('1. Ważona plansza')
        print('2. Punkty, plansza, mobilnosc')
        print('3. Adaptacyjnie: punkty, plansza, mobilnosc')
        black_heuristic = input()
        exe_start_time = time.time()
        AI_vs_AI_mode(5, 5, white_heuristic, black_heuristic)
        exe_end_time = time.time()
        print(exe_end_time - exe_start_time)
    else:
        results = {BLACK: 0, WHITE: 0, "TIE": 0}
        for i in range(0, 4):
            winner = analysis_mode(WHITE, 5, 1)
            results[winner] += 1
        print(results)

        results = {BLACK: 0, WHITE: 0, "TIE": 0}
        for i in range(0, 4):
            winner = analysis_mode(BLACK, 5, 1)
            results[winner] += 1
        print(results)
        print()

        # results = {BLACK: 0, WHITE: 0, "TIE": 0}
        # for i in range(0, 4):
        #     winner = analysis_mode(WHITE, 5, 2)
        #     results[winner] += 1
        # print(results)
        #
        # results = {BLACK: 0, WHITE: 0, "TIE": 0}
        # for i in range(0, 4):
        #     winner = analysis_mode(BLACK, 5, 2)
        #     results[winner] += 1
        # print(results)
        # print()
        #
        # results = {BLACK: 0, WHITE: 0, "TIE": 0}
        # for i in range(0, 4):
        #     winner = analysis_mode(WHITE, 5, 3)
        #     results[winner] += 1
        # print(results)
        #
        # results = {BLACK: 0, WHITE: 0, "TIE": 0}
        # for i in range(0, 4):
        #     winner = analysis_mode(BLACK, 5, 3)
        #     results[winner] += 1
        # print(results)


