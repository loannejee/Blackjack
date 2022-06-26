# Function Defintions:
def take_bet(chips):
    # Since we're asking the user for an integer value, this would be a good place to use try/except
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed ", chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    

def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stay? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player,dealer):
    
    pass
    
def show_all(player,dealer):
    
    pass

def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass
    
def dealer_wins():
    pass
    
def push():
    pass


if __name__ == "__main__":
	print("Functions are run directly.")
else:
	print("Functions are being imported from 'services' module.")

    