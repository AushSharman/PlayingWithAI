def printBoard(dimension: int) -> list:
    dim = []
    for indx in range(dimension):
        dim.append([0] * dimension)
    for row in range(len(dim)):
        print(dim[row][0:])
        print("\n")
    return dim  

def isValidMove(board: list, row: int, col: int) -> bool:
    #check up meaning the col is same but row reduces
    for i in range(row,-1,-1):
        if board[i][col] == 1:
            return False
    #check the left upper diagonal
    for r,c in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[r][c] == 1:
            return False
    #check the right upper diagonal
    for r,c in zip(range(row,-1,-1),range(col+1)):
        if board[r][c] ==1 :
            return False
    return True

def solve(board, row = 0, col = 0):
    dimension = len(board)-1
    if row == dimension and col == dimension:
        return True
    else:
        for position in range(dimension):
            if isValidMove(board,row,col):
                value = solve(board,row+1,col)
                return value
        return False

if __name__ == "__main__":
    board = printBoard(4)
    if solve(board):
        print(board)
    else:
        print("Cannot be solved")