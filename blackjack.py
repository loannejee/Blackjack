import random

# Global variables:
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Dictionary:
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# Single Card Class ===========================================
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        # Gives integer:
        self.value = values[rank]
    
    # What do I want to return when I make an instance?
    def __str__(self):
        return self.rank + " of " + self.suit


# Deck Class ===================================================
class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()