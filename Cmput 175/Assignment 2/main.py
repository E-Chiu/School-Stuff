#----------------------------------------------------
# Assignment 2: Main Program
# 
# Author: Ethan Chiu
# Collaborators: None
# References: Lab 3, Python Documentation, Stack Overflow
#----------------------------------------------------
from UltimateMetaTTT import MetaTicTacToe, ClassicTicTacToe, NumTicTacToe

def showTitle(gameType):
    '''
    displays the title when starting a new game
    Inputs: type of game
    Returns: None
    '''
    border = '-' * 34
    # set the title based on what type of game it is
    if gameType == 'main':
        print(border, '\nStarting New Meta Tic Tac Toe game\n', border)
    elif gameType == 'classic':
        print(border, '\nThis is a Classical Tic Tac Toe')
    elif gameType == 'numeric':
        print(border, '\nThis is a Numerical Tic Tac Toe')

def processInputInt(turn, firstTurn, pool):
    '''
    processes player input until a correct input is given
    Input: row, column inputs
    Returns: row and col as ints
    '''
    success = False
    while not success:
        try:
            if turn == firstTurn:
                number = int(input('Player ' + str(turn) + ' please enter an odd number. (1-9): '))
            else:
                number = int(input('Player ' + str(turn) + ' please enter an even number. (2-8): '))
            # check if number is out of range
            if number < 0 or number > 9:
                print('Error: number is out of range. ', end = '')
            # check if number is correctly odd/even
            elif (turn == firstTurn and (number % 2) == 0) or (turn != firstTurn and (number % 2) != 0):
                if turn == firstTurn:
                    print('Error: entry not odd. ', end = '') 
                else:
                    print('Error: entry not even. ', end = '')
            # check if number has been used before
            elif number not in pool:
                print('Error: that number has already been entered. ', end = '')
            else:
                success = True
        except:
            print('Error: unable to make a move!')
    return number

def processInput(board, turn):
    '''
    processes player input until a correct input is given
    Input: row, column inputs
    Returns: row and col as ints
    '''
    leave = False
    # prompt player to choose a board
    row = input('Player ' + str(turn) + ' please enter a row: ')
    col = input('Player ' + str(turn) + ' please enter a column: ')
    # keep asking for inputs until both are correct
    while not leave:
        try:
            current = 'row'
            row = int(row)
            if row > board.size - 1:
                raise Exception('error')
            current = 'col'
            col = int(col)
            if col > board.size - 1:
                raise Exception('error')
        except:
            # re-ask for input based on which option is incorrect
            if current == 'row':
                row = input('Error: row not in correct range. Player ' + str(turn) + ' please enter a row: ')
            elif current == 'col':
                col = input('Error: column not in correct range. Player ' + str(turn) + ' please enter a column: ')  
        else:
            leave = True
    # return the correct square
    return row, col

def isBoardWon(board, turn):
    '''
    check if board is won
    Inputs: board, turn
    Returns: True or False
    '''
    if board.isWinner():
        board.drawBoard()
        print('Player ' + str(turn) + ' wins. Congrats!')
        return True

def startClassicGame(turn):
    '''
    plays through a classic TTT game
    Inputs: turn
    Returns: winner of the board or D
    '''
    showTitle('classic')
    gameOver = False
    classicBoard = ClassicTicTacToe()
    firstTurn = turn

    while not gameOver:
        classicBoard.drawBoard()

        # get input from user
        row, col = processInput(classicBoard, turn)
        # update board or notify failure
        success = True
        if turn == firstTurn:
            if classicBoard.update(row, col, 'X'):
                gameOver = isBoardWon(classicBoard, turn)
                if gameOver:
                    if turn == 1:
                        return 'X'
                    elif turn == 2:
                        return 'O'
            else:
                print('Error: could not make a move! \n')
                success = False
        else:
            if classicBoard.update(row, col, 'O'):
                if isBoardWon(classicBoard, turn):
                    if turn == 1:
                        return 'X'
                    elif turn == 2:
                        return 'O'
            else:
                print('Error: could not make a move! \n')
                success = False
        # check for tie
        if classicBoard.boardFull():
            classicBoard.drawBoard()
            print("It's a tie.")
            return 'D'
        if success: 
            turn = ((turn) % 2) + 1

def startNumericGame(turn):
    '''
    plays through a numeric TTT game
    Inputs: turn
    Returns: winner of the board or D
    '''
    showTitle('numeric')
    gameOver = False
    numericBoard = NumTicTacToe()
    firstTurn = turn
    pool = [] # pool of possible options
    for i in range(numericBoard.size ** 2):
        pool.append(i + 1)
    while not gameOver:
        numericBoard.drawBoard()

        # get input from user
        number = processInputInt(turn, firstTurn, pool)
        # update board or notify failure
        row, col = processInput(numericBoard, turn)
        if numericBoard.update(row, col, number):
            pool.remove(number)
            if isBoardWon(numericBoard, turn):
                if turn == 1:
                    return 'X'
                elif turn == 2:
                    return 'O'
        # check for tie
        if numericBoard.boardFull():
            numericBoard.drawBoard()
            print("It's a tie.")
            return 'D'
        turn = ((turn) % 2) + 1

def main():
    '''
    Main function for the MetaTTT game
    Inputs: none
    Returns: None
    '''
    showTitle('main')
    gameOver = False
    turn = 1
    metaboard = MetaTicTacToe('configfile')
    success = True
    while not gameOver:
        if success:
            metaboard.drawBoard()
        success = True
        # get the square
        row, col = processInput(metaboard, turn)
        if metaboard.squareIsEmpty(row, col):
            if metaboard.board[row][col] == 'c':
                metaboard.update(row, col, startClassicGame(turn))
            else:
                metaboard.update(row, col, startNumericGame(turn))
            turn = ((turn) % 2) + 1
        else:
            print('Error: could not make a move! ', end = '')
            success = False
        if metaboard.isWinner():
            metaboard.drawBoard()
            print('Player ' + str(turn) + ' wins the Meta Tic Tac Toe Game. GOOD GAME!')
            playAgain = input('Do you want to play another game? (Y/N) ').upper()
            if playAgain != 'Y':
                gameOver = False
    print('\nThanks for playing! Goodbye.')

main()