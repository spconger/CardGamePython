'''
this class represents a player, but it also encapsulates
the hand class I had in the initial diagram. I am really
not sure how a player differs from a hand except for
the name and perhaps score if one wishes to track that
'''
class Player:
    def __init__(self, name, initialscore):
        self.name=name
        self.hand=[]
        self.initialscore=initialscore
        self.currentscore=self.initialscore

    def getname(self):
        return self.name
    
    def addCardtoHand(self, card):
        self.hand.append(card)

    def playCard(self, card):
        index=self.hand.index[card]
        play=self.hand[index]
        self.hand.remove(card)
        return play

    def getHand(self):
        return self.hand
    
    def discardHand(self):
        self.hand=[]

    def addscore(self, points):
        self.currentscore += self.currentscore
        return self.currentscore

    def subtractScore(self, points):
        self.currentscore=self.currentscore-points
        return self.currentscore

    
    def getIntialscore(self):
        return self.initialscore

    def getCurrentscore(self):
        return self.currentscore

    def __str__(self):
        return self.name + "--" + str(self.currentscore)
