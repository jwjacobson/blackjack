#!/usr/bin/python
import time
import sys

class Player:
    def __init__(self, name, points=0, is_dealer=False):
        self.name = name
        self.points = 0
        self.hand = list
        self.is_dealer = is_dealer

    def __str__(self):
        return f"{self.name}"

    def deal(self):                                      # Deal initial hands and report them to user
        self.hand = []
        for i in range(2):
            self.hand.append(deck.pop())                 # Since deck is a set, pop is sufficiently random
        for card in self.hand:
            if self.is_dealer == False:
                print(f"{self} gets {evaluate(card)}.")
            else:                                        # Dealer handled separately because of hidden card
                if card == self.hand[0]:
                    print(f"{self} gets {evaluate(card)}.")
                else:
                    print(f"{self}'s other card is hidden.")

    def get_points(self):                   # Analyze points in hands, including possibility of immediate win
        global tens
        tens = {'a', 'b', 'c', 'd'}         # Set "tens" covers 10, J, Q, K, all of which also cause trouble being evaluated as ints
        for card in self.hand:
            if int(card[0], 16) < 10:       # Integers in number cards under 10 correspond to their value
                self.points += int(card[0])
            elif card[0] in tens:
                self.points += 10
            else:                           # Ace
                self.points += 11
        if self.points == 21:
            print(f"\n{self} gets a Blackjack!")
            print(f"\n{self} wins!")
            return True                     # Returning True used as flag not to continue to next gameplay phase
        if self.is_dealer == False:
            print(f"\n{self} has {self.points} points.")
        else:                               # Dealer handled separately - consequence of hidden card
            global showing_points
            showing_points = self.hand[0][0]
            if showing_points in tens:
                print(f"{self} has 10 points showing.")
                showing_points = 10
                return showing_points       # Return showing_points to be used in hit phase
            elif showing_points == 'e':
                print(f"{self} has 11 points showing.")
                showing_points = 11
                return showing_points
            else:
                print(f"{self} has {showing_points} points showing.")
                showing_points = int(showing_points)
                return showing_points

    def hit(self):                             # Allow players to hit until they win, bust, or stand
        if self.is_dealer:
            while self.points <= 16:           # Dealer will hit until 16 points or bust
                self.hand.append(deck.pop())
                new_card = self.hand[-1]
                global showing_points
                print(f"{self} gets {evaluate(new_card)}.")
                if int(new_card[0], 16) < 10:
                    self.points += int(new_card[0])
                    showing_points += int(new_card[0])
                elif new_card[0] in tens:
                    self.points += 10
                    showing_points += 10
                else:
                    if self.points < 11:
                        self.points += 11
                        showing_points += 11
                    else:
                        self.points += 1
                        showing_points += 1
                print(f"{self} has {showing_points} points showing.")
                if self.value_check():              # value_check returns true if at or over 21; return prevents continuing to "stand"
                    return True
            print(f"\n{self} stands.\n")
        else:
            answers = "yn"
            prompt = input("\nHit? (y/n) ")
            prompt = prompt.lower()
            while prompt not in answers:
                prompt = input("Answer [Y]es or [N]o. ")
            while prompt == "y":
                self.hand.append(deck.pop())
                new_card = self.hand[-1]
                print(f"{self} gets {evaluate(new_card)}.")
                if int(new_card[0], 16) < 10:
                    self.points += int(new_card[0])
                elif new_card[0] in tens:
                    self.points += 10
                else:
                    if self.points < 11:
                        self.points += 11
                    else:
                        self.points += 1
                print(f"{self} has {self.points} points.")
                if self.value_check():
                    return True
                prompt = input("\nHit again? (y/n) ")
                prompt = prompt.lower()
                while prompt not in answers:
                    prompt = input("Answer [Y]es or [N]o. ")
                if prompt == 'n':
                    break
                else:
                    continue
            print(f"{self} stands.")
    
    def value_check(self):              # Check if players have won or busted after each hit
        if self.points == 21:
            print(f"{self} gets 21!")
            print(f"{self} wins!")
            return True
        elif self.points > 21:
            print(f"{self} goes bust!")
            if self.is_dealer:
                print(f"({self}'s other card was {evaluate(self.hand[0])}.)")
            return True
        else:
            return False

    def reveal(self, player):               # Only runs if both players stand (haven't won or busted)
        hidden_card = self.hand[0]
        print(f"{self} had {evaluate(hidden_card)}.") # Reveal dealer's hidden card and total points
        print(f"{self} had {self.points} points.")
        if self.points > player.points:
            print(f"{self} wins!")
        elif player.points > self.points:
            print("Player wins!")
        else:
            print("A tie! No one wins...")

def play_again(player1, player2):
    global game
    prompt = input("\nPlay again? (y/n) ")
    while prompt.lower() != "n" and prompt.lower() != "y":
        prompt = input("Choose [Y] or [N]. ")
    if prompt.lower() == "y":
        player1.points = 0              # Reset points
        player2.points = 0
        global deck
        if len(deck) < 10:              # Recreate deck if less than 10 cards
            print("\nReshuffling...")
            shuffle()
        game = True                     # Continue gameplay loop
    else:
        game = False                    # End
        print("Goodbye.")

def shuffle():                          # Create deck
    global deck
    deck = set()                        # Set pop functionality obviates need for random
    for i in range(13):
        deck.add(hex(i+2)[2:] + "S")    # Cards stored as 2-character string, converted to human readable by evaluate() (below)
        deck.add(hex(i+2)[2:] + "H")
        deck.add(hex(i+2)[2:] + "D")
        deck.add(hex(i+2)[2:] + "C")
    return deck

def get_length():                       # Report number of cards remaining (possibly useful for card counters)
    global deck
    print(f"\nThere are {len(deck)} cards left in the deck.\n")

def evaluate(card):                     # Convert 2-character card string into human-readable string
    if int(card[0], 16) < 10:
        value = card[0]
    elif card[0] == "a":
        value = "10"
    elif card[0] == "b":
        value = "Jack"
    elif card[0] == "c":
        value = "Queen"
    elif card[0] == "d":
        value = "King"
    else:
        value = "Ace"
    if value:
        if card[1]  == "S":
            suit = "Spades"
        elif card[1]  == "H":
            suit = "Hearts"
        elif card[1]  == "D":
            suit = "Diamonds"
        elif card[1]  == "C":
            suit = "Clubs"
    return f"the {value} of {suit}"

def menu():                                  # Title screen and opening menu
    sprint1("\u001b[43;1m\\\u001b[0m"*50 + "\n")
    sprint1("\u001b[43;1m "*20 + "BLACKJACK " + "\u001b[43;1m \u001b[0m"*20 + "\n")
    sprint1("\u001b[43;1m/\u001b[0m"*50 + "\n\n")
    rest(1)
    sprint2(quote1)
    rest(.25)
    sprint2(quote2)
    rest(.25)
    sprint2(quote3)
    rest(2)
    sprint2(quote4)
    rest(2)
    global game
    prompt = input("\n\n[N]ew game or [Q]uit? ")
    while prompt.lower() != "n" and prompt.lower() != "q":
        prompt = input("Choose [N] or [Q]. ")
    if prompt.lower() == "n":
        game = True
    else:
        game = False
        print("Goodbye.")

def sprint1(s):             # Character-by-character printing for analog effect
    for c in s:             # source: https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line 
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)
def sprint2(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)

# Rest adds time between execution of commands for more human-scale timing 
def rest(x):
    time.sleep(x*0.5)

quote1 = "\u001b[33;1mWhat separates blackjack from other games\n"
quote2 = "is that it's based on dependent events,\n"
quote3 = "meaning past affects the probability in the future.\n"
quote4 = "- William Tell, The Card Counter (2021)\u001b[0m"


def main():
    player = Player("Player")                       # Create players
    dealer = Player("Dealer", is_dealer=True)       #
    shuffle()                                       # Create deck
    menu()                                          # Play or quit
    while game:                                     # Gameplay loop
        get_length()                                # Report cards remaining in deck
        player.deal()                               # Deal cards
        dealer.deal()                               #
        if not player.get_points():                 # Only continue to next gameplay phase if no one has won/lost yet
            if dealer.get_points() != True:         # Specify != True because dealer.get_points() returns showing_points int
                if not player.hit():
                    if not dealer.hit():
                        dealer.reveal(player)
        play_again(player, dealer)

main()