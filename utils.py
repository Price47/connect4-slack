import exceptions


def gen_new_board(rows=6, cols=7):
    # return [[None]*cols]*rows
    return [[0] * cols for i in range(rows)]


def place_piece(board, column, player):
    column_idx = column - 1
    for i in range(1, len(board) + 1):
        # Find the next open spot to play
        if board[-i][column_idx] == 0:
            board[-i][column_idx] = player
            # Player placed a piece, move is over
            break
    else:
        raise exceptions.ColumnFull
    return board


def check_win(board, col_played):
    col_played_idx = col_played - 1

    for row_idx in range(len(board)):
        if board[row_idx][col_played_idx] != 0:
            # Found the last move played
            last_move = {'r': row_idx, 'c': col_played_idx}
            break

    player = board[last_move['r']][last_move['c']]

    ###
    # Check horizontal
    ###
    count = 0
    # Check left
    for col_idx in range(col_played_idx - 1, -1, -1):
        if board[last_move['r']][col_idx] == player:
            count += 1
            continue
        break

    # Check right
    for col_idx in range(col_played_idx + 1, len(board[0])):
        if board[last_move['r']][col_idx] == player:
            count += 1
            continue
        break

    # Check if win
    if count >= 3:
        return True

    ###
    # Check vertical
    ###
    count = 0
    # Only need to check down
    for row_idx in range(last_move['r'] + 1, len(board)):
        if board[row_idx][last_move['c']] == player:
            count += 1
            continue
        break

    # Check if win
    if count >= 3:
        return True

    ###
    # Check diagonal /
    ###
    count = 0
    # Check down-left
    for i in range(1, 4):  # Only need to check the next 3 spots
        try:
            if board[last_move['r'] + i][last_move['c'] - i] == player:
                count += 1
                continue
        except IndexError:
            break
        break

    # Check up-right
    for i in range(1, 4):  # Only need to check the next 3 spots
        try:
            if board[last_move['r'] - i][last_move['c'] + i] == player:
                count += 1
                continue
        except IndexError:
            break
        break

    # Check if win
    if count >= 3:
        return True

    ###
    # Check diagonal \
    ###
    count = 0
    # Check up-left
    for i in range(1, 4):  # Only need to check the next 3 spots
        try:
            if board[last_move['r'] - i][last_move['c'] - i] == player:
                count += 1
                continue
        except IndexError:
            break
        break

    # Check down-right
    for i in range(1, 4):  # Only need to check the next 3 spots
        try:
            if board[last_move['r'] + i][last_move['c'] + i] == player:
                count += 1
                continue
        except IndexError:
            break
        break

    # Check if win
    if count >= 3:
        return True

    return False