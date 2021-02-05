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


def checkColors(board: list) -> bool:
    startingRow = 0
    startingColumn = 4
    for row in range(5):
        numbers = []
        cells = [(startingRow, startingColumn), 
                 (startingRow+1, startingColumn),
                 (startingRow+2, startingColumn),
                 (startingRow+3, startingColumn),
                 (startingRow+4, startingColumn),
                 (startingRow+4, startingColumn+1),
                 (startingRow+4, startingColumn+2),
                 (startingRow+4, startingColumn+3),
                 (startingRow+4, startingColumn+4)]
        for cell in cells:
            currentCell = board[cell[0]][cell[1]]
            if currentCell != ' ' and currentCell != "*":
                numbers.append(currentCell)
        if len(numbers) != len(set(numbers)):
            return False

        startingRow += 1
        startingColumn -= 1
    return True

def validateBoard(board: list) -> bool:
    if checkColors(board) and checkColumns(board) and checkRows(board):
        return True
    return Falses