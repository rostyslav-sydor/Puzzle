def checkColumns(board: list) -> bool:
    """
    Returns true if there is no repeating numbers in the columns
    """
    for i in range(9):
        column = []
        for line in board:
            if line[i].isnumeric():
                column.append(line[i])
        if len(column) != len(set(column)):
            return False
    return True
