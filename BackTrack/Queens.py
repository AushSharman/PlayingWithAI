def printBoard(dimension: int) -> list:
    dim = []
    for indx in range(dimension):
        dim.append([0] * dimension)
    for row in range(len(dim)):
        print(dim[row][0:])
        print("\n")
    return dim  

def isValidMove(board: list, row: int, col: int) -> bool:
    #print(row ," is row and col us ", col)
    #check up meaning the col is same but row reduces
    for i in range(row,-1,-1):
        if board[i][col] == 1:
            return False
    #check the left upper diagonal meaning both row and col decrease
    for r,c in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[r][c] == 1:
            return False
    #check the right upper diagonal meaning that row decreases and col increases
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
            if isValidMove(board,row,position):
                board[row][position] = 1
                print(board)
                value = solve(board,row+1,position+1)
            board[row][position] = 0
        return False

if __name__ == "__main__":
    board = printBoard(4)
    if solve(board):
        print(board)
    else:
        print("Cannot be solved")

#TODO: Adjust the alogorithim as output is incorrect 