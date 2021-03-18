#----------------------------------------------------
# Assignment 3: Spite and Malice Classes
# 
# Author: Ethan Chiu
# Collaborators: None
# References: Python Documentation, Stack Overflow, Class Slides
#----------------------------------------------------

import random
from lectureStructures import Stack, CircularQueue

class Card:
    '''
    class for the cards to be used in Spite and Malice
    '''
    def __init__(self, value):
        '''
        initializes a card with a face and value
        input: value
        output: none or assertion error
        '''
        self.__cardPool = []
        for i in range(-1, 10):
            self.__cardPool.append(i)
        assert value in self.__cardPool, "invalid value"
        if value == -1:
            self.__face = '*'
        else:
            self.__face = str(value)
        self.__value = value
    
    def assign(self, value):
        '''
        assigns a new value, only if it is a joker card
        input: new value
        output: none or assertion error
        '''
        assert value in self.__cardPool, "Error: Invalid value"
        if self.__face != '*':
            raise Exception("Error: Not a joker")
        self.__value = value

    def getValue(self):
        '''
        returns the value of the card
        input: none
        output: value
        '''
        return self.__value
    
    def getFace(self):
        '''
        returns the face of the card
        input: none
        output: face
        '''
        return self.__face

    def __str__(self):
        '''
        returns string format of the card
        input: none
        output: card as a string
        '''
        return '[' + self.__face + ']'

    def __repr__(self):
        '''
        returns representation of the card
        input: none
        output: representation of the card
        '''
        return str(self) + '.' + str(self.__value)

class PlayStack:
    '''
    class for the stack of playing cards
    '''
    def __init__(self):
        '''
        initializes a stack
        input: none
        output: none
        '''
        self.cards = Stack()

    def peekValue(self):
        '''
        returns top of the stack if possible
        input: none
        output: top of the stack or error
        '''
        try:
            return self.cards.peek().getValue()
        except:
            raise Exception("Error: No cards in the playing stack")

    def peekFace(self):
        try:
            return self.cards.peek().getFace()
        except:
            raise Exception("Error: No cards in the playing stack")

    def playCard(self, card):
        '''
        adds a card to the stack
        input: card
        output: none, or error
        '''
        # check if the card is a zero on an empty stack
        if self.cards.isEmpty() and card.getValue() == 0:
            self.cards.push(card)
            return []
        # check if the card is a joker
        if card.getValue() == -1:
            # playing on empty stack
            if self.cards.isEmpty():
                card.assign(0)
                self.cards.push(card)
                return []
            # playing on non-empty stack
            else:
                card.assign(self.cards.peek().getValue() + 1)
                self.cards.push(card)
                if card.getValue() == 9:
                    temp = []
                    for i in range(self.cards.size()):
                        temp.append(self.cards.pop().getFace())
                    return temp
                else:
                    return []
        # check if the card is one value higher
        elif not self.cards.isEmpty() and card.getValue() == self.cards.peek().getValue() + 1:
            self.cards.push(card)
            if card.getValue() == 9:
                temp = []
                for i in range(self.cards.size()):
                    temp.append(self.cards.pop().getFace())
                return temp
            else:
                return []
        else:
            raise Exception("Error: Card rejected")

    def __str__(self):
        '''
        returns string format of the stack
        input: none
        output: stack as a string
        '''
        output = ['|']
        returnStack = Stack()
        for i in range(self.cards.size()):
            temp = self.cards.pop()
            output.append(str(temp))
            returnStack.push(temp)
        for i in range(returnStack.size()):
            self.cards.push(returnStack.pop())
        output.append('|')
        output.reverse()
        return ''.join(output)

class Hand:
    '''
    class for your hand of cards
    '''
    def __init__(self):
        '''
        initializes a list for your hand of cards
        '''
        self.__hand = []
        self.__size = 0
        self.__capacity = 5

    def sort(self):
        '''
        sorts the hand of cards
        input: none
        output: none
        '''
        for i in range(1, self.getSize()):
            temp = self.__hand[i]
            insertInd = i
            while insertInd > 0 and self.__hand[insertInd - 1].getValue() > temp.getValue():
                self.__hand[insertInd] = self.__hand[insertInd - 1]
                insertInd -= 1
            self.__hand[insertInd] = temp

    def pop(self, i = -1):
        '''
        discards card from the hand if possible
        input: none or index of card to discard
        output: none or error message
        '''
        if i == -1:
            assert len(self.__hand) > 0, "Error: Nothing to discard"
            popCard = self.__hand.pop(i)
        else:
            assert i >= 0 and i < len(self.__hand), "Error: Out of range"
            popCard = self.__hand.pop(i)
        self.__size -= 1
        return popCard
    
    def index(self, v):
        '''
        returns the index of the card of a certain value
        input: value to find
        output: index of the card or lack thereof
        '''
        counter = 0
        for card in self.__hand:
            if card.getValue() == v:
                return counter
            counter += 1
        return -1
    
    def check0(self):
        '''
        returns the index of the first 0 card
        input: none
        output: index of the card or lack thereof
        '''
        return self.index(0)

    def getSize(self):
        '''
        returns the hand size
        input: none
        output: size of hand
        '''
        return self.__size

    def add(self, cardList):
        '''
        adds a list of cards to the hand
        input: cards to add
        output: none or error
        '''
        assert len(cardList) <= self.__capacity - self.__size, 'Error: Too many cards'
        for card in cardList:
            self.__hand.append(card)
            self.__size += 1
    
    def __str__(self):
        '''
        converts hand into a string format
        input: none
        output: hand as a string
        '''
        output = '['
        for i in range(self.__size):
            output += '[' + self.__hand[i].getFace() + ']'
        output += ']'
        return output

def shuffle(cardList):
    returnList = []
    while len(cardList) > 0:
        returnList.append(cardList.pop(random.randrange(0, len(cardList))))
    return returnList