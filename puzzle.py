def checkColumns(board: list) -> bool:
    """
    Returns True if there is no repeating numbers in the columns.
    """
    for i in range(len(board[0])):
        column = []
        for line in board:
            if line[i].isnumeric():
                column.append(line[i])
        if len(column) != len(set(column)):
            return False
    return True


def checkRows(board: list) -> bool:
    """
    Returns True if there is no repeating numbers in the rows.
    """
    for row in board:
        numbersRow = row.replace('*', '').replace(' ', '')
        if len(numbersRow) != len(set(numbersRow)):
            return False
    return True
