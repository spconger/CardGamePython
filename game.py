from abc import ABC, abstractmethod
from card import Card
from deck import Deck
import random
'''
Not entirely sure of this yet. The idea is to create a template
for almost any card game.
The class is abstract because it inherits from ABC
which makes abstract classes. It has both abstract
and concrete methods. Abstract methods are decorated with
@abstractmethod, and must be implemented by the inheriting
class. They will also get the concrete classes which can
be accessed by the source keyword.
What I am not sure about is the stucture of what should
make up a generic card game. This could take some
more thought.
I have startGame(), turn() and endgame as abstract methods
I also have methods to set the deck, get the deck, shuffle it
and deal
'''

class Game(ABC):
    def __init__(self, name):
        self.name=name
        self.deck=[]

    #set the conditions for starting the game
    @abstractmethod
    def startGame(self):
        pass

    #code what is involved in a turn
    @abstractmethod
    def turn(self):
        pass

    #What conditions end the game
    @abstractmethod
    def endGame(self):
        pass

    #set the deck by passing it in
    def setDeck(self, deck):
        self.deck=deck

    #return the deck
    def getDeck(self):
        return self.deck

    def shuffleDeck(self):
        #suffle the deck
        randDeck=self.getDeck()
        random.shuffle(randDeck)
        return randDeck

    def deal(self,number):
        #get a shuffled deck
        self.newDeck=self.shuffleDeck()
        #create an empty list for the hand
        self.hand=[]
        #if there are more cards in the deck
        #than the number requestd
        if number < len(self.newDeck):
            #get that number of cards
            #and put them in the hand list
            for i in range(number):
                self.hand.append(self.newDeck[i])
            #remove those cards from the
                #suffled deck
            for c in self.hand:
                self.newDeck.remove(c)
        #return the hand      
        return self.hand

    def __str__(self):
        return self.name