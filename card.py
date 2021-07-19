#Card
'''
This class represents a playing care. It has a rank and suit.
The rank is a number between 1 and 13, 1 being an ace and 13
being a king. The value is not set because that depends upon
the game context, though the getValue() method, if called
assigns the usually assumed values.
The suit is generally Hearts, clubs, diamonds
and spades,and is passed in via a single character.
The suit and the rank are passed in with the constructor.
The getSuite() method takes the character and translates it
into the complete name for the suit
The string method translates the suite and the rank
into the usual name of the card such as 'ace of spaces'
or 'queen of hearts.'
'''
class Card:
    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit
        self.value=0
       
    #return the rank    
    def getRank(self):
        return self.rank
        
    #return the suit
    def getSuit(self):
        return self.suit

    #get the play value of the card
    def getValue(self):
        if self.rank > 10:
            self.value=10
        else:
            self.value=self.rank
        return self.value

   #get the suite name
    def getSuitName(self):
        self.su=""
        if self.suit =="d":
            self.su="diamonds"
        elif self.suit=="h":
            self.su="hearts"
        elif self.suit=="s":
            self.su="spades"
        else:
            self.su ="clubs"
        return self.su

    
    #use the rank and suit to return the name of the card.
    def __str__(self):
        
        if self.rank >1 and self.rank< 11:
            self.name=str(self.rank) + " of " + self.getSuit()
        if self.rank==1:
            self.name="the ace of " + self.getSuitName()
        if self.rank==11:
            self.name="the jack of " + self.getSuitName()
        if self.rank==12:
             self.name="the queen of " + self.getSuitName()
        if self.rank==13:
             self.name="the king of " + self.getSuitName()
        return self.name