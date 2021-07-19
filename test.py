import unittest
from card import Card
from deck import Deck

class testCard(unittest.TestCase):
    def setUp(self):
        self.card=Card(11,'d')

    def test_getRank(self):
        self.assertEqual(self.card.getRank(), 11)

    def test_getSuit(self):
        self.assertEqual(self.card.getSuit(), 'd')

    def test_getValue(self):
        self.assertEqual(self.card.getValue(), 10)

    def test_getSuitName(self):
        self.assertEqual(self.card.getSuitName(), 'diamonds')

    def test_string(self):
        self.assertEqual(str(self.card), "the jack of diamonds")

class testDeck(unittest.TestCase):
    def setUp(self):
        self.deck=Deck()

    def test_InitialCount(self):
        d=self.deck.getDeck()
        self.assertEqual(len(d), 52)
    
    def test_card(self):
        cards = self.deck.getDeck()
        card=cards[13]
        self.assertEqual(str(card),'the ace of hearts')

    def test_lastcard(self):
        cards = self.deck.getDeck()
        card=cards[51]
        self.assertEqual(str(card),'the king of spades')