import random
import services

# Global variables:
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Dictionary:
suits = {'Hearts':'♥️', 'Diamonds':'♦️', 'Spades':'♠️', 'Clubs':'♣️'}
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 11}


# Single Card Class ===========================================
class Card:

    def __init__(self, suit, rank):
        self.suit = suits[suit]
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
    
    def deal(self):
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
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        # If a hand's value exceeds 21 but it contains an Ace, we can reduce the Ace's value from 11 to 1 and continue playing.
        while self.value > 21 and self.aces:
            # Make the ace a 1 instead of 11:
            self.value -= 10
            self.aces -= 1

# Chips Class ===================================================
class Chips:
    
    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# Play the Game =================================================
playing = True

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    services.take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    services.show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        services.hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        services.show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            services.player_busts(player_hand,dealer_hand,player_chips)
            break 

   # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            services.hit(deck,dealer_hand)    
    
        # Show all cards
        services.show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            services.dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            services.dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            services.player_wins(player_hand,dealer_hand,player_chips)

        else:
            services.push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break