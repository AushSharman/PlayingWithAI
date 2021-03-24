#display the board and return it so we can alter it
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
    #check the left upper diagonal meaning both row and col decrease
    for r,c in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[r][c] == 1:
            return False
    #check the right upper diagonal meaning that row decreases and col increases
    for r,c in zip(range(row,-1,-1),range(col,len(board)-1)):
        if board[r][c] ==1 :
            return False
    return True

#main chunker of the program 
def solve(board, row = 0) -> tuple:
    dimension = len(board)
    #base case is if row is the length of the actual board (which doesnt exist), return True cuz all queens are places
    if row == dimension :
        return (True,board)
    else:
        for position in range(dimension):
            #call checker for each valid row and col
            if isValidMove(board,row,position):
                board[row][position] = 1
                value,b = solve(board,row+1)
                if value: return (value,b)
            board[row][position] = 0
    return (False,board)


#driver program
if __name__ == "__main__":
    dimension = int(input("Enter the dimension of the board: "))
    value,board = solve(printBoard(dimension))
    if (dimension == 2 or dimension == 3):
        print("Cannot be solved")
    else:
        for i in board:
            print(i)

#LEZZZ GO!!!