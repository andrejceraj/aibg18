ROWS = 6
COLS = 7

def check_horizontal(table, current_turn):
    curr_row, curr_col = current_turn
    val = table[curr_row][curr_col]

    counter = 0
    for j in range(curr_col, COLS):
        if table[curr_row][j] == val:
            counter += 1
        else:
            break
    if counter >= 4:
        return True

    counter = 0
    for j in reversed(range(0, curr_col + 1)):
        if table[curr_row][j] == val:
            counter += 1
        else:
            break
    if counter >= 4:
        return True

    return False


def check_vertical(table, current_turn):
    curr_row, curr_col = current_turn
    val = table[curr_row][curr_col]

    counter = 0
    for i in range(curr_row, ROWS):
        if table[i][curr_col] == val:
            counter += 1
        else:
            break
    if counter >= 4:
        return True

    counter = 0
    for i in reversed(range(0, curr_row + 1)):
        if table[i][curr_col] == val:
            counter += 1
        else:
            break
    if counter >= 4:
        return True

    return False


def check_diagonal(table, current_turn):
    curr_row, curr_col = current_turn
    val = table[curr_row][curr_col]

    counter = 0
    i, j = curr_row, curr_col
    while i < ROWS and j < COLS:
        if table[i][j] == val:
            counter += 1
        else:
            break
        i += 1
        j += 1
    if counter >= 4:
        return True

    counter = 0
    i, j = curr_row, curr_col
    while i < ROWS and j > 0:
        if table[i][j] == val:
            counter += 1
        else:
            break
        i += 1
        j -= 1
    if counter >= 4:
        return True

    counter = 0
    i, j = curr_row, curr_col
    while i > 0 and j < COLS:
        if table[i][j] == val:
            counter += 1
        else:
            break
        i -= 1
        j += 1
    if counter >= 4:
        return True

    counter = 0
    i, j = curr_row, curr_col
    while i > 0 and j > 0:
        if table[i][j] == val:
            counter += 1
        else:
            break
        i -= 1
        j -= 1
    if counter >= 4:
        return True

    return False


def is_table_filled(table):
    for i in range(len(table[0])):
        if table[0][i] == 0:
            return False
    return True
