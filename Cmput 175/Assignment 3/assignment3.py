#----------------------------------------------------
# Assignment 3: Spite and Malice Game
# 
# Author: Ethan Chiu
# Collaborators: None
# References: Python Documentation, Stack Overflow, Class Slides

# IMPORTANT: there is a bug where the program crashes after discarding
# at random times and I was unable to recreate it, but I tried
# fixing it and it hasn't shown up after several tests so I think
# it is fine. Just a heads up.
#----------------------------------------------------
import random
from spiteAndMalice import Card, PlayStack, Hand, shuffle, Stack, CircularQueue

def setup():
    '''
    sets up things needed for the game
    input: none
    output: card shoe, player piles, player hands
    '''
    cardPool = []
    shoeSize = 120
    handSize = 5
    gameStacksNum = 4
    discardStacksNum = 4
    cardSize = 10
    goalSize = 15
    # initialize the deck of 120 cards
    for i in range(cardSize):
        cardPool.append(Card(-1))
        cardPool.append(Card(-1))
        for j in range(cardSize):
            cardPool.append(Card(j))
    # shuffle the cards
    cardPool = shuffle(cardPool)
    # deal cards to both players
    # make a stack for each player
    player1Goal = Stack()
    player2Goal = Stack()
    # make a hand for each player
    player1Hand = Hand()
    player2Hand = Hand()
    # add cards to the stack and hand from the pool
    for i in range(handSize):
        player1Hand.add([cardPool.pop()])
        player2Hand.add([cardPool.pop()])
    for i in range(goalSize):
        player1Goal.push(cardPool.pop())
        player2Goal.push(cardPool.pop())
    # add the remaining cards to a shoe queue
    cardShoe = CircularQueue(shoeSize)
    for card in cardPool:
        cardShoe.enqueue(card)
    # make a nested list of 4 playstacks
    gameStacks =[]
    for i in range(gameStacksNum):
        gameStacks.append(PlayStack())
    # make discard stacks
    player1Discard = []
    player2Discard = []
    for i in range(discardStacksNum):
        player1Discard.append(Stack())
        player2Discard.append(Stack())
    # make sets of lists for the player properties
    goalList = [player1Goal, player2Goal]
    handList = [player1Hand, player2Hand]
    discardList = [player1Discard, player2Discard]
    return cardShoe, goalList, handList, discardList, gameStacks

def determineFirst(goalList):
    '''
    determines who goes first at the start of a game
    input: player goalStacks
    output: who's turn it is
    '''
    player1Goal = goalList[0]
    player2Goal = goalList[1]
    if player1Goal.peek().getValue() == -1:
        p1Val = 10
    else:
        p1Val = player1Goal.peek().getValue()
    if player2Goal.peek().getValue() == -1:
        p2Val = 10
    else:
        p2Val = player2Goal.peek().getValue()
    if p1Val > p2Val or p1Val == p2Val:
        return 0
    else:
        return 1

def showBoard(goalList, handList, gameStacks, discardList):
    '''
    shows the current state of the board
    input: goal list, hand list, stack list, discard list
    output: none
    '''
    players = ['A', 'B']
    output = '-' * 40
    for i in range(len(discardList)):
        # print hand
        handList[i].sort() # sort the hand beforehand
        output += '\nPlayer' + players[i] + ' Hand ' + str(handList[i])
        # print discard stack
        for j in range(len(discardList[i])):
            output += '\nPlayer' + players[i] + ' Discard ' + str(j + 1) + ': [' + stringStack(discardList[i][j]) + ']'
        # print goal
        if goalList[i].size() > 0:
            output += '\nPlayer' + players[i] + ' Goal [' + goalList[i].peek().getFace() + '] ' + str(goalList[i].size()) + ' cards left'
        else:
            output += '\nPlayer' + players[i] + ' Goal [ ] ' + str(goalList[i].size()) + ' cards left'
        # print playstacks
        if i < len(discardList) - 1:
            output += '\n\n'
            for j in range(len(gameStacks)):
                output += 'Play Stack ' + str(j + 1) + ' : ' + str(gameStacks[j]) + '\n'
        output += '\n'
    output += '-' * 40
    print(output)

def drawPhase(turn, handList, cardShoe, tempList, emptyNum):
    '''
    check if player needs to draw cards and draws cards if applicable
    input: player turn, player hands, and shoe
    output: tempList and emptyNum
    '''
    # check if the shoe has enough cards
    if cardShoe.size() < (5 - handList[turn].getSize()):
        # if not enough cards shuffle back
        shuffleBack(tempList, cardShoe)
        tempList = []
        emptyNum = 0
    toAdd = []
    for i in range(5 - handList[turn].getSize()):
        toAdd.append(cardShoe.dequeue())
    handList[turn].add(toAdd)
    return tempList, emptyNum

def playPhase(turn, goalList, handList, gameStacks, discardList, zero, emptyNum, tempList):
    '''
    player plays cards until it is no longer possible/they wish to stop
    inputs: turn, goals, hands, stacks, discards, whether there is a zero, # of emptied stacks and tempList
    output: # of emptied stacks and tempList
    '''
    endLoop = False
    while not endLoop:
        try:
            # ask what move the player wishes to do
            move = input('Play from where: hi = hand at position i (1..4); g = goal; dj = discard pile j (1..4)?\n').lower()
            # check for invalid inputs
            # check input
            assert (('d' in move or 'h' in move) and len(move) == 2)  or 'g' in move, 'Error: Invalid input'
            # get location if from hand or discard
            if 'd' in move or 'h' in move:
                getLocation = int(move[1]) - 1
                # check input
                assert getLocation >= 0 and getLocation < 5, 'Error: out of Range'
            # check if they need to play a zero
            if zero and emptyStack(gameStacks):
                assert not 'd' in move, 'Error: Must play zero'
                assert not (move == 'g'  and goalList[turn].peek().getValue() != 0), 'Error: Must play zero'
                assert not ('h' in move and handList[turn].check0() != getLocation), 'Error: Must play zero'
            # if correct input then ask where to play the card and check that input
            setLocation = int(input('Which Play Stack are you targeting (1..4)?')) - 1 
            assert setLocation >= 0 and setLocation < len(gameStacks), "Error: Out of range"
            # get the card to push
            if 'g' in move:
                card = goalList[turn].pop()
            elif 'h' in move:
                card = handList[turn].pop(getLocation)
            elif 'd' in move:
                card = discardList[turn][getLocation].pop()
            # add the card to the stack 
            getList = gameStacks[setLocation].playCard(card)
            # if stack was emptied add to a temporary stack
            if getList != []:
                tempList += getList
                emptyNum += 1
        # print any needed exceptions
        except AssertionError as e:
            print(e)
        except Exception as e:
            # return the card back if it was rejected
            try:
                if 'g' in move:
                    goalList[turn].push(card)
                elif 'h' in move:
                    handList[turn].add([card])
                elif 'd' in move:
                    discardList[turn][getLocation].push(card)
                print(e)
            except:
                # if another error just print generic error
                print('Error: Invalid Input')
        finally:
            endLoop = True
    return tempList, emptyNum

def endPhase(turn, handList, discardList):
    '''
    prompts the user to discard any cards and ends the turn
    inputs: turn, hands, discards
    output: none
    '''
    endLoop = False
    while not endLoop:
        # end turn without asking if hand is empty or full of zeros
        if handList[turn].getSize() == 0 or allZero(handList[turn]):
            return
        try:
            # ask player where to discard from
            setLocation = int(input('Which Discard Pile are you targeting (1..4)?')) - 1
            # check input
            assert setLocation >= 0 and setLocation < 4, 'Error: Out of range'
            # get card to discard
            getLocation = int(input('Which card are you discarding? (1..5)?')) - 1
            # check input
            assert getLocation >= 0 and getLocation < handList[turn].getSize(), 'Error: Out of range'
            # if inputs are correct do the discard
            card = handList[turn].pop(getLocation)
            discardList[turn][setLocation].push(card)
            endLoop = True
        except AssertionError as e:
            print(e)
        except Exception as e:
            print('Error: Invalid Input')

def hasZero(turn, goalList, handList):
    '''
    checks to see if player has a 0 in goal or hand
    inputs: turn, player hands, player goals
    outputs: boolean
    '''
    if handList[turn].check0() != -1:
        return True
    if goalList[turn].peek().getValue() == 0:
        return True
    return False

def allZero(hand):
    '''
    checks to see if whole hand is 0
    inputs: hand
    outputs: boolean
    '''
    # check if first and last cards are both zero
    temp = hand.pop()
    hand.add([temp])
    if hand.check0() == 0 and temp.getValue == 0:
        return True
    else:
        return False

def emptyStack(gameStacks):
    '''
    checks to see if there is any empty playing stack
    inputs: stacks
    output: boolean
    '''
    for stack in gameStacks:
        if stack.cards.isEmpty():
            return True
    return False

def shuffleBack(tempList, cardShoe):
    '''
    takes tempList and makes new cards to shuffle back into shoe
    input: tempList, cardShoe
    output: none
    '''
    tempList = shuffle(tempList) # shuffle the cards
    for face in tempList:
        # enqueue the cards back into the shoe
        if face == '*':
            cardShoe.enqueue(Card(-1))
        else:
            cardShoe.enqueue(Card(int(face)))

def stringStack(stack):
    '''
    returns the string format of contents in a stack. Used for discard piles
    input: stack
    output: string of contents
    '''
    tempStack = Stack() # stack to add back to existing stack
    output = []
    # remove from stack and add to string and temp stack
    for i in range(stack.size()):
        card = stack.pop()
        tempStack.push(card)
        output.append(str(card))
    # add back to original
    for i in range(tempStack.size()):
        stack.push(tempStack.pop())
    output.reverse()
    return ''.join(output)

def checkWinner(goalList):
    '''
    checks to see if a player has emptied their goal stack:
    input: goal list
    output: boolean
    '''
    for goal in goalList:
        if goal.isEmpty():
            return True
    return False

def main():
    '''
    controls the main flow of the game
    input: none
    output: none
    '''
    cardShoe, goalList, handList, discardList, gameStacks = setup()
    playerList = ['A', 'B'] # characters to be used
    turn = determineFirst(goalList)
    gameOver = False
    # used to store emptied stacks before adding back to shoe
    emptyNum = 0
    tempList = []
    while not gameOver:
        # draw cards
        tempList, emptyNum = drawPhase(turn, handList, cardShoe, tempList, emptyNum)
        # ask player what to do next
        endLoop = False
        while not endLoop:
            # show the board
            showBoard(goalList, handList, gameStacks, discardList)
            move = input('Player' + playerList[turn] + ', choose action: p (play) or x (discard/end turn) \n').lower()
            if move == 'p':
                # enter the playing phase
                tempList, emptyNum = playPhase(turn, goalList, handList, gameStacks, discardList, hasZero(turn, goalList, handList), emptyNum, tempList)
                # if 5 stacks have been emptied add back to the shoe
                if emptyNum == 1:
                    shuffleBack(tempList, cardShoe)
                    tempList = []
                    emptyNum = 0
            elif move == 'x':
                # check if they have zero that needs to be played
                if hasZero(turn, goalList, handList) and emptyStack(gameStacks):
                    print('Error: Must play zero')
                else:
                    # enter the end phase
                    endPhase(turn, handList, discardList)
                    endLoop = True
                    # switch the turn
                    turn = (turn + 1) % 2
            else:
                print('Error: Invalid option')
            # check for a winner
            if checkWinner(goalList):
                # if there is a winner end the game
                print('Player' + playerList[turn - 1], ' has won the game! Congratulations!')
                replay = input('Play again? (Y/N)').lower()
                if replay == 'y':
                    # if playing again reset everything
                    cardShoe, goalList, handList, discardList, gameStacks = setup()
                    tempList = []
                    emptyNum = 0
                else:
                    endLoop = True
                    gameOver = True

main()