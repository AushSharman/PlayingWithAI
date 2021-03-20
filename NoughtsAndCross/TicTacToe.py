import random
import time
gameBoard = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}


def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")

def isEmpty(board: list) -> bool:
    return " " in list(board.values())

def isSpaceFree(board: list, pos: int) -> bool:
    return board[pos] == " "

def isWinner(board, mark):
    winningPositions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [
        1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for pos in winningPositions:
        one, two, three = pos
        if board[one] == board[two] == board[three] == mark:
            return True
    return False

def randomBot():
    return random.randint(1,9)

def makeMove(board: list, player: str, num: int):
    board[num] = player

def game():
    print("Welcome to Tic Tac Toe")
    play = input("Do you wish to play? [Yes or No]")
    if play[0].lower() == "y":
        numBot = input("Choose the bot of your type [Random Bot or MinMax Bot]: ")
        printBoard(gameBoard)
        player1,player2 = "X","O"
        current = player1
        while(isEmpty(gameBoard)):
            number = int(input("Enter a number [1-9]")) if current==player1 else numBot
            while ((number <= 0 or number > 9) or not isSpaceFree(gameBoard, number)):
                try:
                    if current == player1:
                        print("Invalid input - try again")
                    number = int(input("Enter a number [1-9] ")) if current==player1 else randomBot() 
                except:
                    if current == player1:
                        print("Invalid input - try again")
                    number = int(input("Enter a number [1-9] ")) if current==player1 else randomBot()

            makeMove(gameBoard,current, number)
            printBoard(gameBoard)
            if isWinner(gameBoard, current):
                print(f"Congrats {current}, You won the game!!")
                break
            current = player2 if current==player1 else player1

        if not isEmpty(gameBoard) and not isWinner(gameBoard,player1) and not isWinner(gameBoard,player2):
            print("Tie game")

if __name__ == '__main__':
    game()
