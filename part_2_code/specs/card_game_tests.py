import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card('Hearts', 1)  # initialize card1
        self.card2 = Card('Diamonds', 10)  # initialize card2
        self.game = CardGame()  # initialize game, if necessary

    def test_check_for_ace(self):
        self.card1.value = 1
        self.assertTrue(self.game.check_for_ace(self.card1))  # test when card is ace
        self.card1.value = 2
        self.assertFalse(self.game.check_for_ace(self.card1))  # test when card is not ace

    def test_highest_card(self):
        self.card1.value = 2
        self.card2.value = 3
        self.assertEqual(self.game.highest_card(self.card1, self.card2), self.card2)  # card2 is higher
        self.card1.value = 4
        self.assertEqual(self.game.highest_card(self.card1, self.card2), self.card1)  # card1 is higher

    def test_cards_total(self):
        cards = [self.card1, self.card2]
        self.card1.value = 2
        self.card2.value = 3
        self.assertEqual(self.game.cards_total(cards), "You have a total of 5")  # 2 + 3 = 5

if __name__ == "__main__":
    unittest.main()