import random

# Global variables:
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Dictionary:
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 11}


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
        self.deck = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.deck.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal_one(self):
        return self.deck.pop()


# Hand Class ===================================================
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
    
    def adjust_for_ace(self):
        # If a hand's value exceeds 21 but it contains an Ace, we can reduce the Ace's value from 11 to 1 and continue playing.
        while self.value > 21 and self.aces:
            # Make the ace a 1 instead of 11:
            self.value -= 10
            self.aces -= 1

# Chips Class ===================================================
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# Setup New Game =================================================
new_deck = Deck()
new_deck.shuffle()

human_player = Hand()
computer_player = Hand()


# Play the Game =================================================
playing = True

while playing:
    pass