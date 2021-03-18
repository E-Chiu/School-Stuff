#----------------------------------------------------
# Assignment 2: Tic Tac Toe classes
# 
# Author: Ethan Chiu
# Collaborators: None
# References: Lab 3, Python Documentation, Stack Overflow
#----------------------------------------------------
class SkeletonTTT:
    def __init__(self):
        '''
        Parent class for the other ttt boards
        Inputs: none
        Returns: None
        '''
        self.size = 3 # size of board
        self.board = [] # nested list for the game
        for row in range(self.size):
                self.board.append([])
                for col in range(self.size):
                    self.board[row].append(0)
    

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains a number 
        greater than 0.
        Inputs:
        row (int) - row index of square to check
        col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        instances = ['c', 'n']
        return self.board[row][col] == 0 or self.board[row][col] in instances


    def update(self, row, col, mark):
        '''
        Assigns the integer, mark, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row, col):
            self.board[row][col] = mark
            return True
        else:
            return False


    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        instances = ['c','n']
        for row in self.board:
            for square in row:
                if square == 0 or square in instances:
                    return False
        return True


class NumTicTacToe(SkeletonTTT):
    pass
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        rowNum = 0
        space = '   '
        print()
        for i in range(self.size):
            print(space + str(i), end ='')
        print()
        for row in self.board:
            print(str(rowNum) + ' ', end = '')
            colNum = 0
            for square in row:
                if square == 0:
                    print('   ', end = '')
                else:
                    print(' ' + str(square) + ' ', end = '')
                if colNum < self.size - 1:
                    print('|', end = '')
                colNum += 1
            if rowNum < self.size - 1:
                print('\n' + '  -----------')
            rowNum += 1
        print()


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        return super().squareIsEmpty(row, col)
    
    
    def update(self, row, col, mark):
        '''
        Assigns the integer, mark, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        return super().update(row, col, mark)
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        return super().boardFull()
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # loop through rows to check
        for row in self.board:
            if sum(row) == 15 and 0 not in row:
                return True
        # Make a list for columns and diagonals and check individually
        for i in range(self.size):
            colList = []
            for j in range(self.size):
                colList.append(self.board[j][i])
            if 0 not in colList:
                if sum(colList) == 15:
                    return True
        diagList = []
        for i in range(self.size):
            diagList.append(self.board[i][i])
        if 0 not in diagList:
            if sum(diagList) == 15:
                return True
        diagList = []
        for i in range(self.size):
            diagList.append(self.board[self.size - 1 - i][i])
        if 0 not in diagList:
            if sum(diagList) == 15:
                return True
        return False
    
    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: True
        '''
        return True     
    
    
class ClassicTicTacToe(SkeletonTTT):
    pass
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        rowNum = 0
        space = '   '
        print()
        for i in range(self.size):
            print(space + str(i), end ='')
        print()
        for row in self.board:
            print(str(rowNum) + ' ', end = '')
            colNum = 0
            for square in row:
                if square == 0:
                    print('   ', end = '')
                else:
                    print(' ' + square + ' ', end = '')
                if colNum < self.size - 1:
                    print('|', end = '')
                colNum += 1
            if rowNum < self.size - 1:
                print('\n' + '  -----------')
            rowNum += 1
        print()


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains an X or O.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        return super().squareIsEmpty(row, col)
    
    
    def update(self, row, col, mark):
        '''
        Assigns the string, mark, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        return super().update(row, col, mark)
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        return super().boardFull()
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) with 
        matching marks (i.e. 3 Xs  or 3 Os). That line can be horizontal, vertical,
        or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # loop through rows to check
        for row in self.board:
            if ('X' not in row or 'O' not in row) and 0 not in row:
                return True
        # Make a list for columns and diagonals and check individually
        for i in range(self.size):
            colList = []
            for square in range(self.size):
                for j in range(self.size):
                    colList.append(self.board[j][i])
            if ('X' not in colList or 'O' not in colList) and 0 not in colList:
                return True
        diagList = []
        for i in range(self.size):
            diagList.append(self.board[i][i])
        if ('X' not in diagList or 'O' not in diagList) and 0 not in diagList:
            return True
        diagList = []
        for i in range(self.size):
            diagList.append(self.board[self.size - 1 - i][i])
        if ('X' not in diagList or 'O' not in diagList) and 0 not in diagList:
            return True
        return False
    
    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: False
        '''
        return False 


class MetaTicTacToe(SkeletonTTT):
    def __init__(self, configFile):
        '''
        Initializes an empty Meta Tic Tac Toe board, based on the contents of a 
        configuration file.
        Inputs: 
           configFile (str) - name of a text file containing configuration information
        Returns: None
        '''
        self.board = []
        self.size = 3
        boardFile = open(configFile, 'r')
        lines = boardFile.readlines()
        # initialize 2d list
        for row in range(self.size):
            self.board.append([])
        # split each lines into individual characters, then add them to board list
        for line in lines:
            boardTypes = line.replace('\n', '')
            boardTypes = boardTypes.replace(' ', '')
            i = 0
            for boardType in boardTypes:
                self.board[i].append(boardType)
                i += 1
        boardFile.close()
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        rowNum = 0
        space = '   '
        print()
        for i in range(self.size):
            print(space + str(i), end ='')
        print()
        for row in self.board:
            print(str(rowNum) + ' ', end = '')
            colNum = 0
            for square in row:
                print(' ' + square + ' ', end = '')
                if colNum < self.size - 1:
                    print('|', end = '')
                colNum += 1
            if rowNum < self.size - 1:
                print('\n' + '  -----------')
            rowNum += 1   
        print()


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square contains a non-played local game board ("empty"),
        or the result of a played local game board (not "empty").
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        return super().squareIsEmpty(row, col)
    
    
    def update(self, row, col, result):
        '''
        Assigns the string, result, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           result (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        return super().update(row, col, result)
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares (i.e. any un-played
        local boards).
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        return super().boardFull()
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) of their
        mark (three Xs for Player 1, three Os for Player 2), or 3 draws. That line
        can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # loop through rows to check
        for row in self.board:
            if ('X' not in row or 'O' not in row or 'D' not in row) and ('n' not in row and 'c' not in row):
                return True
        # Make a list for columns and diagonals and check individually
        for i in range(self.size):
            colList = []
            for j in range(self.size):
                colList.append(self.board[j][i])
            if 0 not in colList:
                if ('X' not in colList or 'O' not in colList or 'D' not in colList) and ('n' not in colList and 'c' not in colList):
                    return True
        diagList = []
        for i in range(self.size):
            diagList.append(self.board[i][i])
        if 0 not in diagList:
            if ('X' not in diagList or 'O' not in diagList or 'D' not in diagList) and ('n' not in diagList and 'c' not in diagList):                
                return True
        diagList = []
        for i in range(self.size):
            diagList.append(self.board[self.size - 1 - i][i])
        if 0 not in diagList:
            if ('X' not in diagList or 'O' not in diagList or 'D' not in diagList) and ('n' not in diagList and 'c' not in diagList):
                return True
        return False
    
    def getLocalBoard(self, row, col):
        '''
        Returns the instance of the empty local board at the specified row, col 
        location (i.e. either ClassicTicTacToe or NumTicTacToe).
        Inputs:
           row (int) - row index of square
           col (int) - column index of square
        Returns: instance of appropriate empty local board if un-played; 
                 None if local board has already been played
        '''
        instances = ['c','n']
        if self.board[row][col] not in instances:
            return None
        else:
            return self.board[row][col]

# function to clear the board (for tests only)
def clearBoard(ttt):
        for i in range(ttt.size):
            for j in range(ttt.size):
                ttt.board[i][j] = 0

# clear function for meta ttt
def clearMain(ttt, configfile):
    ttt.board = []
    boardFile = open(configfile, 'r')
    lines = boardFile.readlines()
    # initialize 2d list
    for row in range(ttt.size):
        ttt.board.append([])
    # split each lines into individual characters, then add them to board list
    for line in lines:
        boardTypes = line.replace('\n', '')
        boardTypes = boardTypes.replace(' ', '')
        i = 0
        for boardType in boardTypes:
            ttt.board[i].append(boardType)
            i += 1
    boardFile.close()

if __name__ == "__main__":
    # Tests for the meta board
    print('TESTS FOR META TTT BEGIN')
    # initialize an preset board
    metaBoard = MetaTicTacToe('configfile')
    metaBoard.drawBoard()
    # update a square
    print('assigning')
    metaBoard.update(1,2,'X')
    metaBoard.drawBoard()
    # check if squares are empty
    print('Checking if empty')
    print(metaBoard.squareIsEmpty(0,0))
    print(metaBoard.squareIsEmpty(1,2))
    # asign a result to a non empty square
    print('\ntrying to overwrite')
    metaBoard.update(1,2,'O')
    metaBoard.drawBoard()
    # check if the board has a winner
    print('is there a winner?')
    print(metaBoard.isWinner())
    # check if the board is full
    print('\nis the board full?')
    print(metaBoard.boardFull())
    # add values to the board so that any line matches 
    metaBoard.update(0,0,'X')
    metaBoard.update(0,1,'X')
    metaBoard.update(0,2,'X')
    metaBoard.drawBoard()
    # check if the board has a winner
    print('is there a winner?')
    print(metaBoard.isWinner())
    # check if the board is full
    print('\nis the board full?')
    print(metaBoard.boardFull())
    # check every row, col, diag that it checks for a win
    clearMain(metaBoard, 'configfile')
    for i in range(3):
        for j in range(3):
            metaBoard.update(i,j,'X')
        metaBoard.drawBoard()
        print('is there a winner?')
        print(metaBoard.isWinner())
        clearMain(metaBoard, 'configfile')
    for i in range(3):
        for j in range(3):
            metaBoard.update(j,i,'X')
        metaBoard.drawBoard()
        print('is there a winner?')
        print(metaBoard.isWinner())
        clearMain(metaBoard, 'configfile')
    metaBoard.update(0,0,'X')
    metaBoard.update(1,1,'X')
    metaBoard.update(2,2,'X')
    metaBoard.drawBoard()
    print('is there a winner?')
    print(metaBoard.isWinner())
    clearMain(metaBoard, 'configfile')
    metaBoard.update(0,2,'X')
    metaBoard.update(1,1,'X')
    metaBoard.update(2,0,'X')
    metaBoard.drawBoard()
    print('is there a winner?')
    print(metaBoard.isWinner())
    clearMain(metaBoard, 'configfile')
    # check that if one square is empty will not print win
    metaBoard.update(0,2,'X')
    metaBoard.update(2,0,'X')
    metaBoard.drawBoard()
    print('is there a winner?')
    print(metaBoard.isWinner())
    clearMain(metaBoard, 'configfile')


    # For num TTT
    print('\nTESTS FOR NUMERIC TTT BEGIN')
    # initialize empty board
    numBoard = NumTicTacToe()
    print('\nContents of board attribute when object first created:')
    print(numBoard.board)
    numBoard.drawBoard()
    # assign a number to an empty square and display
    print('assigning')
    numBoard.update(1,2,1)
    numBoard.drawBoard()
    #check if squares are empty
    print('checking if empty')
    print(numBoard.squareIsEmpty(0,0))
    print(numBoard.squareIsEmpty(1,2))
    # assign a number to a non-empty square
    print('\ntrying to overwrite')
    numBoard.update(1,2,2)
    numBoard.drawBoard()
    # making sure numbers can't be reused
    print('trying to reuse a number')
    numBoard.update(0,0,1)
    # check if the board has a winner
    print('\nis there a winner?')
    print(numBoard.isWinner())
    # check if the board is full
    print('\nis the board full?')
    print(numBoard.boardFull())
    # add values to the board so that any line adds up to 15
    numBoard.update(0,0,5)
    numBoard.update(0,1,5)
    numBoard.update(0,2,5)
    numBoard.drawBoard()
    # check if the board has a winner
    print('there a winner?')
    print(numBoard.isWinner())
    # check if the board is full
    print('\nis the board full?')
    print(numBoard.boardFull())
    # check if board is full
    for i in range(3):
        for j in range(3):
            numBoard.update(i,j,5)
    numBoard.drawBoard()
    print('is the board full?')
    print(numBoard.boardFull())
    # check every row, col, diag that it checks for a win
    clearBoard(numBoard)
    for i in range(3):
        for j in range(3):
            numBoard.update(i,j,5)
        numBoard.drawBoard()
        print('is there a winner?')
        print(numBoard.isWinner())
        clearBoard(numBoard)
    for i in range(3):
        for j in range(3):
            numBoard.update(j,i,5)
        numBoard.drawBoard()
        print('is there a winner?')
        print(numBoard.isWinner())
        clearBoard(numBoard)
    numBoard.update(0,0,5)
    numBoard.update(1,1,5)
    numBoard.update(2,2,5)
    numBoard.drawBoard()
    print('is there a winner?')
    print(numBoard.isWinner())
    clearBoard(numBoard)
    numBoard.update(0,2,5)
    numBoard.update(1,1,5)
    numBoard.update(2,0,5)
    numBoard.drawBoard()
    print('is there a winner?')
    print(numBoard.isWinner())
    clearBoard(numBoard)
    # check that if one square is empty will not print win
    numBoard.update(0,2,9)
    numBoard.update(2,0,6)
    numBoard.drawBoard()
    print('is there a winner?')
    print(numBoard.isWinner())
    clearBoard(numBoard)

    # For classic TTT
    print('\n TESTS FOR CLASSIC TTT BEGIN')
    # initialize empty board
    classicBoard = ClassicTicTacToe()
    print('\nContents of board attribute when object first created:')
    print(classicBoard.board)
    classicBoard.drawBoard()
    # assign a value to an empty square and display
    print('assigning')
    classicBoard.update(1,2,'X')
    classicBoard.drawBoard()
    #check if squares are empty
    print('checking if empty')
    print(classicBoard.squareIsEmpty(0,0))
    print(classicBoard.squareIsEmpty(1,2))
    # assign a value to a non-empty square
    print('\ntrying to overwrite')
    classicBoard.update(1,2,'O')
    classicBoard.drawBoard()
    # check if the board has a winner
    print('is there a winner?')
    print(classicBoard.isWinner())
    # check if the board is full
    print('\nis the board full?')
    print(classicBoard.boardFull())
    # add values to the board so that any line matches 
    classicBoard.update(0,0,'X')
    classicBoard.update(0,1,'X')
    classicBoard.update(0,2,'X')
    classicBoard.drawBoard()
    # check if the board has a winner
    print('is there a winner?')
    print(classicBoard.isWinner())
    # check if the board is full
    print('\nis the board full?')
    print(classicBoard.boardFull())
    # check every row, col, diag that it checks for a win
    clearBoard(classicBoard)
    for i in range(3):
        for j in range(3):
            classicBoard.update(i,j,'X')
        classicBoard.drawBoard()
        print('is there a winner?')
        print(classicBoard.isWinner())
        clearBoard(classicBoard)
    for i in range(3):
        for j in range(3):
            classicBoard.update(j,i,'X')
        classicBoard.drawBoard()
        print('is there a winner?')
        print(classicBoard.isWinner())
        clearBoard(classicBoard)
    classicBoard.update(0,0,'X')
    classicBoard.update(1,1,'X')
    classicBoard.update(2,2,'X')
    classicBoard.drawBoard()
    print('is there a winner?')
    print(classicBoard.isWinner())
    clearBoard(classicBoard)
    classicBoard.update(0,2,'X')
    classicBoard.update(1,1,'X')
    classicBoard.update(2,0,'X')
    classicBoard.drawBoard()
    print('is there a winner?')
    print(classicBoard.isWinner())
    clearBoard(classicBoard)
    # check that if one square is empty will not print win
    classicBoard.update(0,2,'X')
    classicBoard.update(2,0,'X')
    classicBoard.drawBoard()
    print('is there a winner?')
    print(classicBoard.isWinner())
    clearBoard(classicBoard)
