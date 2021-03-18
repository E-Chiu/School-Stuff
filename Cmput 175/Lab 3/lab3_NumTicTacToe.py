#----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
# 
# Author: 
# Collaborators:
# References:
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        rowNum = 0
        print('\n   0   1   2')
        for row in self.board:
            print(str(rowNum) + ' ', end = '')
            colNum = 0
            for col in row:
                if col == 0:
                    print('   ', end = '')
                else:
                    print(' ' + str(col) + ' ', end = '')
                if colNum < 2:
                    print('|', end = '')
                colNum += 1
            if rowNum < 2:
                print('\n' + '  -----------')
            rowNum += 1
        # TO DO: delete pass and print out formatted board
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |           

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        if self.board[row][col] == 0:
            return True
        else:
            return False
        # TO DO: delete pass and complete method
    
    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row, col) and num < 10:
            self.board[row][col] = num
            return True
        else:
            return False
        # TO DO: delete pass and complete method
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        return True

        # TO DO: delete pass and complete method
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        for row in self.board:
            if sum(row) == 15 and 0 not in row:
                return True
        for i in range(3):
            colTup = (self.board[0][i], self.board[1][i], self.board[2][i])
            if 0 not in colTup:
                if sum(colTup) == 15:
                    return True
        diagTup = (self.board[0][0], self.board[1][1], self.board[2][2])
        if 0 not in diagTup:
            if sum(diagTup) == 15:
                return True
        diagTup = (self.board[2][0], self.board[1][1], self.board[0][2])
        if 0 not in diagTup:
            if sum(diagTup) == 15:
                return True
        return False
        # TO DO: delete pass and complete method
     
def clearBoard():
    for i in range(3):
        for j in range(3):
            myBoard.board[i][j] = 0

if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required
    
    # start by creating empty board and checking the contents of the board attribute
    myBoard = NumTicTacToe()
    print('Contents of board attribute when object first created:')
    print(myBoard.board)
    
    # does the empty board display properly?
    myBoard.drawBoard()

    # assign a number to an empty square and display
    myBoard.update(1,2,9)
    myBoard.drawBoard()
    # try to assign a number to a non-empty square. What happens?
    myBoard.update(1,2,3)
    myBoard.drawBoard()
    # check if the board has a winner. Should there be a winner after only 1 entry?
    print('\n', myBoard.isWinner())
    # check if the board is full. Should it be full after only 1 entry?
    print('\n', myBoard.boardFull())
    # add values to the board so that any line adds up to 15. Display
    myBoard.update(0,0,5)
    myBoard.update(0,1,5)
    myBoard.update(0,2,5)
    myBoard.drawBoard()
    # check if the board has a winner
    print('\n', myBoard.isWinner())
    # check if the board is full
    print('\n', myBoard.boardFull())
    # write additional tests, as needed
    # check every row, col, diag that it checks for a win
    clearBoard()
    for i in range(3):
        for j in range(3):
            myBoard.update(i,j,5)
        myBoard.drawBoard()
        print('\n', myBoard.isWinner())
        clearBoard()
    for i in range(3):
        for j in range(3):
            myBoard.update(j,i,5)
        myBoard.drawBoard()
        print('\n', myBoard.isWinner())
        clearBoard()
    myBoard.update(0,0,5)
    myBoard.update(1,1,5)
    myBoard.update(2,2,5)
    myBoard.drawBoard()
    print('\n', myBoard.isWinner())
    clearBoard()
    myBoard.update(0,2,5)
    myBoard.update(1,1,5)
    myBoard.update(2,0,5)
    myBoard.drawBoard()
    print('\n', myBoard.isWinner())
    clearBoard()
    # check that if one cell is empty will not print win
    myBoard.update(0,2,5)
    myBoard.update(2,0,5)
    myBoard.drawBoard()
    print('\n', myBoard.isWinner())
    clearBoard()


    
