#Import the Card and the Random
#classes
from card import Card
import random

'''
A deck is a collection or list of cards.
The init peforms several activities
it sets up what is essentially a enum of suits,
an array, then it defines an empty list of cards.
Finally it calls the method to initialize the deck
to a standard 52 card deck. The method getDeck returns 
the list of cards. setCards() allows a game or user
to pass in a custome deck.
'''

class Deck:
    def __init__(self):
        #initialize the suits
        self.suits=["d","h","c","s"]
        #initialize the card list
        self.cards=[]
        #call the initializeDeck method
        #self.initializeDeck()
        
   
    def initializeDeck(self):
        #this method populates the cards List
        #with cards
        #loop through the suits
        for i in range(4):
            suit=self.suits[i]
            #loop through the ranks
            for x in range(1,14):
                rank=x 
                #create a card
                c=Card(rank,suit)
                #add to list of cards
                self.cards.append(c)
                
    def getDeck(self):
        #return a deck
        self.initializeDeck()
        return self.cards

    def setDeck(self, cards):
        self.cards = cards
        
'''

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
'''