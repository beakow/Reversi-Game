from reversi import *


weighted_board = [[100, -20, 10,  5,  5, 10, -20, 100],
                  [-20, -50, -2, -2, -2, -2, -50, -20],
                  [ 10,  -2, -1, -1, -1, -1,  -2,  10],
                  [  5,  -2, -1, -1, -1, -1,  -2,   5],
                  [  5,  -2, -1, -1, -1, -1,  -2,   5],
                  [ 10,  -2, -1, -1, -1, -1,  -2,  10],
                  [-20, -50, -2, -2, -2, -2, -50, -20],
                  [100, -20,  10, 5,  5, 10, -20, 100]]


def strategy1(board, maximizing_color):
    minimizing_color = get_other_color(maximizing_color)
    score_max = 0
    score_min = 0
    for row in range(0, 8):
        for col in range(0, 8):
            if board[row][col] == maximizing_color:
                score_max += weighted_board[row][col]
            elif board[row][col] == minimizing_color:
                score_min += weighted_board[row][col]
    return score_max - score_min


def points_ratio(board, maximizing_color):
    minimizing_color = get_other_color(maximizing_color)
    score_max = get_score(board, maximizing_color)
    score_min = get_score(board, minimizing_color)
    if (score_max + score_min) != 0:
        return ((score_max - score_min) / (score_max + score_min)) * 100
    return 0


def corners(board, maximizing_color):
    minimizing_color = get_other_color(maximizing_color)
    corner_count_max = 0
    corner_count_min = 0
    for x, y in [(0, 0), (0, 7), (7, 0), (7, 7)]:
        if board[y][x] == maximizing_color:
            corner_count_max += 1
        elif board[y][x] == minimizing_color:
            corner_count_min += 1
    if (corner_count_max + corner_count_min) != 0:
        return ((corner_count_max - corner_count_min) / (corner_count_max + corner_count_min)) * 100
    return 0


def edges(board, maximizing_color):
    minimizing_color = get_other_color(maximizing_color)
    edge_count_max = 0
    edge_count_min = 0
    for x, y in [(0, i) for i in range(2, 6)] + [(6, i) for i in range(2, 6)] + [(i, 0) for i in range(2, 6)] + [(i, 6) for i in range(2, 6)]:
        if board[y][x] == maximizing_color:
            edge_count_max += 1
        elif board[y][x] == minimizing_color:
            edge_count_min += 1
    if (edge_count_max + edge_count_min) != 0:
        return ((edge_count_max - edge_count_min) / (edge_count_max + edge_count_min)) * 100
    return 0


def mobility(board, maximizing_color):
    minimizing_color = get_other_color(maximizing_color)
    moves_max = len(get_available_moves(board, maximizing_color))
    moves_min = len(get_available_moves(board, minimizing_color))
    if (moves_max + moves_min) != 0:
        return ((moves_max - moves_min) / (moves_max + moves_min)) * 100
    return 0


def strategy2(board, maximizing_color):
    score = 0
    score += points_ratio(board, maximizing_color) * 4
    score += corners(board, maximizing_color) * 5
    score += edges(board, maximizing_color) * 2
    score += mobility(board, maximizing_color) * 2
    return score


def strategy3(board, maximizing_color):
    board_usage = ((get_score(board, WHITE) + get_score(board, BLACK)) / 64) * 100
    if board_usage < 30:
        weights = {"points_ratio": 2,
                   "corners": 5,
                   "edges": 2,
                   "mobility": 1}
    elif board_usage < 50:
        weights = {"points_ratio": 3,
                   "corners": 5,
                   "edges": 2,
                   "mobility": 2}
    elif board_usage < 80:
        weights = {"points_ratio": 4,
                   "corners": 5,
                   "edges": 3,
                   "mobility": 4}
    else:
        weights = {"points_ratio": 5,
                   "corners": 1,
                   "edges": 1,
                   "mobility": 5}
    score = 0
    score += points_ratio(board, maximizing_color) * weights["points_ratio"]
    score += corners(board, maximizing_color) * weights["corners"]
    score += edges(board, maximizing_color) * weights["edges"]
    score += mobility(board, maximizing_color) * weights["mobility"]
    return score
