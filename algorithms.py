import random

from heuristics import *


def minimax(board, depth, root_move, next_move, color, maximizing_color, strategy):
    (row, col) = next_move
    new_board = board.copy()
    new_board = place_disk(new_board, row, col, color)
    additional_move = has_additional_move(new_board, color)

    if is_game_over(new_board) or depth == 0:
        if strategy == 1:
            result = strategy1(new_board, maximizing_color)
        elif strategy == 2:
            result = strategy2(new_board, maximizing_color)
        else:
            result = strategy3(new_board, maximizing_color)
        return result, root_move, additional_move
    else:
        next_turn_color = color if additional_move else get_other_color(color)
        available_moves = get_available_moves(new_board, next_turn_color)
        best_root_move = None
        additional_move = False
        if maximizing_color == color:
            max_eval = float('-inf')
            for move in available_moves:
                if move is not None:
                    (max_eval_cand, best_root_move_cand, additional_move_cand) = \
                        minimax(new_board, depth - 1, root_move, move, next_turn_color, maximizing_color, strategy)
                    if max_eval_cand > max_eval or (max_eval_cand == max_eval and additional_move_cand):
                        max_eval = max_eval_cand
                        best_root_move = best_root_move_cand
                        additional_move = additional_move_cand
            return max_eval, best_root_move, additional_move
        else:
            min_eval = float('inf')
            for move in available_moves:
                if move is not None:
                    (min_eval_cand, best_root_move_cand, additional_move_cand) = \
                        minimax(new_board, depth - 1, root_move, move, next_turn_color, maximizing_color, strategy)
                    if min_eval_cand < min_eval or (min_eval_cand == min_eval and additional_move_cand):
                        min_eval = min_eval_cand
                        best_root_move = best_root_move_cand
                        additional_move = additional_move_cand
            return min_eval, best_root_move, additional_move


def minimax_alpha_beta(board, depth, root_move, next_move, color, maximizing_color, alpha, beta, strategy):
    (row, col) = next_move
    new_board = board.copy()
    new_board = place_disk(new_board, row, col, color)
    additional_move = has_additional_move(new_board, color)

    if is_game_over(new_board) or depth == 0:
        if strategy == 1:
            result = strategy1(new_board, maximizing_color)
        elif strategy == 2:
            result = strategy2(new_board, maximizing_color)
        else:
            result = strategy3(new_board, maximizing_color)
        return result, root_move, additional_move
    else:
        next_turn_color = color if additional_move else get_other_color(color)
        available_moves = get_available_moves(new_board, next_turn_color)
        best_root_move = None
        additional_move = False
        if maximizing_color == color:
            max_eval = float('-inf')
            for move in available_moves:
                if move is not None:
                    (max_eval_cand, best_root_move_cand, additional_move_cand) = \
                        minimax_alpha_beta(new_board, depth - 1, root_move, move, next_turn_color, maximizing_color, alpha, beta, strategy)
                    if max_eval_cand > max_eval or (max_eval_cand == max_eval and additional_move_cand):
                        max_eval = max_eval_cand
                        best_root_move = best_root_move_cand
                        additional_move = additional_move_cand
                    if max_eval >= beta:
                        return max_eval, best_root_move, additional_move
                    if max_eval > alpha:
                        alpha = max_eval
            return max_eval, best_root_move, additional_move
        else:
            min_eval = float('inf')
            for move in available_moves:
                if move is not None:
                    (min_eval_cand, best_root_move_cand, additional_move_cand) = \
                        minimax_alpha_beta(new_board, depth - 1, root_move, move, next_turn_color, maximizing_color, alpha, beta, strategy)
                    if min_eval_cand < min_eval or (min_eval_cand == min_eval and additional_move_cand):
                        min_eval = min_eval_cand
                        best_root_move = best_root_move_cand
                        additional_move = additional_move_cand
                    if min_eval <= alpha:
                        return min_eval, best_root_move, additional_move
                    if min_eval < beta:
                        beta = min_eval
            return min_eval, best_root_move, additional_move


def get_best_move(board, color, depth, strategy):
    available_moves = get_available_moves(board, color)
    max_eval = float('-inf')
    best_root_move = None
    for move in available_moves:
        (max_eval_cand, best_root_move_cand, additional_move_cand) = minimax(board, depth, move, move, color, color, strategy)
            # minimax_alpha_beta(board, depth, move, move, color, color, float('-inf'), float('inf'), strategy)

        if max_eval_cand > max_eval or (max_eval_cand == max_eval and additional_move_cand):
            max_eval = max_eval_cand
            best_root_move = best_root_move_cand

    return best_root_move


def get_random_move(board, color):
    available_moves = get_available_moves(board, color)
    move = random.choice(available_moves)

    return move
