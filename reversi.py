WHITE = '⚪'
BLACK = '🔴'
EMPTY = '⚫'


def get_other_color(color):
    if color == WHITE:
        return BLACK
    elif color == BLACK:
        return WHITE


def initialize_game():
    board = [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY, WHITE, BLACK, EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]
    return board, True, WHITE


def disks_to_change_color(board, row, col, color):
    change_list = []
    other_color = get_other_color(color)

    # up
    i = row - 1
    j = col
    change_list_cand = []
    found = False
    while i >= 0:
        if board[i][j] == other_color:
            change_list_cand.append((i, j))
            i -= 1
        elif board[i][j] == color:
            found = True
            break
        else:
            break
    if found:
        change_list = change_list + change_list_cand
    else:
        change_list_cand.clear()

    # down
    i = row + 1
    j = col
    change_list_cand = []
    found = False
    while i < 8:
        if board[i][j] == other_color:
            change_list_cand.append((i, j))
            i += 1
        elif board[i][j] == color:
            found = True
            break
        else:
            break
    if found:
        change_list = change_list + change_list_cand
    else:
        change_list_cand.clear()

    # left
    i = row
    j = col - 1
    change_list_cand = []
    found = False
    while j >= 0:
        if board[i][j] == other_color:
            change_list_cand.append((i, j))
            j -= 1
        elif board[i][j] == color:
            found = True
            break
        else:
            break
    if found:
        change_list = change_list + change_list_cand
    else:
        change_list_cand.clear()

    # right
    i = row
    j = col + 1
    change_list_cand = []
    found = False
    while j < 8:
        if board[i][j] == other_color:
            change_list_cand.append((i, j))
            j += 1
        elif board[i][j] == color:
            found = True
            break
        else:
            break
    if found:
        change_list = change_list + change_list_cand
    else:
        change_list_cand.clear()

    # up left
    i = row - 1
    j = col - 1
    change_list_cand = []
    found = False
    while i >= 0 and j >= 0:
        if board[i][j] == other_color:
            change_list_cand.append((i, j))
            i -= 1
            j -= 1
        elif board[i][j] == color:
            found = True
            break
        else:
            break
    if found:
        change_list = change_list + change_list_cand
    else:
        change_list_cand.clear()

    # down left
    i = row + 1
    j = col - 1
    change_list_cand = []
    found = False
    while i < 8 and j >= 0:
        if board[i][j] == other_color:
            change_list_cand.append((i, j))
            i += 1
            j -= 1
        elif board[i][j] == color:
            found = True
            break
        else:
            break
    if found:
        change_list = change_list + change_list_cand
    else:
        change_list_cand.clear()

    # up right
    i = row - 1
    j = col + 1
    change_list_cand = []
    found = False
    while i >= 0 and j < 8:
        if board[i][j] == other_color:
            change_list_cand.append((i, j))
            i -= 1
            j += 1
        elif board[i][j] == color:
            found = True
            break
        else:
            break
    if found:
        change_list = change_list + change_list_cand
    else:
        change_list_cand.clear()

    # down left
    i = row + 1
    j = col + 1
    change_list_cand = []
    found = False
    while i < 8 and j < 8:
        if board[i][j] == other_color:
            change_list_cand.append((i, j))
            i += 1
            j += 1
        elif board[i][j] == color:
            found = True
            break
        else:
            break
    if found:
        change_list = change_list + change_list_cand
    else:
        change_list_cand.clear()

    return change_list


def get_available_moves(board, color, ):
    available_moves = []
    for row in range(0, 8):
        for col in range(0, 8):
            if board[row][col] == EMPTY:
                change_list = disks_to_change_color(board, row, col, color)
                if len(change_list) > 0:
                    available_moves.append((row, col))
    return available_moves


def is_game_over(board):
    b = 0
    w = 0
    empty = 0
    for row in range(0, 8):
        for col in range(0, 8):
            if board[row][col] == WHITE:
                w += 1
            elif board[row][col] == BLACK:
                b += 1
            else:
                empty += 1

    if b == 0 or w == 0 or empty == 0:
        return True

    w_available_moves = get_available_moves(board, WHITE)
    b_available_moves = get_available_moves(board, BLACK)
    return len(w_available_moves) == 0 and len(b_available_moves) == 0


def place_disk(board, row, col, color):
    new_board = [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]
    for i in range(0, 8):
        for j in range(0, 8):
            new_board[i][j] = board[i][j]
    new_board[row][col] = color
    change_list = disks_to_change_color(new_board, row, col, color)
    for (i, j) in change_list:
        new_board[i][j] = color
    return new_board


def has_additional_move(board, color):
    other_color = get_other_color(color)
    other_color_moves = get_available_moves(board, other_color)
    return len(other_color_moves) == 0


def get_score(board, color):
    score = 0
    for row in range(0, 8):
        for col in range(0, 8):
            if board[row][col] == color:
                score += 1
    return score
