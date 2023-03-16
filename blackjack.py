#!/usr/bin/python
"""
What separates blackjack from other games
is that it's based on dependent events,
meaning past affects the probability in the future.
- William Tell, The Card Counter
"""

class Player:
    def __init__(self, name, stand=False, points=0, is_dealer=False):
        self.name = name
        self.points = 0
        self.hand = list
        self.is_dealer = is_dealer
        self.stand = stand

    def __str__(self):
        return f"{self.name}"

    def deal(self):
        self.hand = []
        for i in range(2):
            self.hand.append(deck.pop())
        for card in self.hand:
            if self.is_dealer == False:
                print(f"{self} gets {evaluate(card)}.")
            else:
                if card == self.hand[0]:
                    print(f"{self} gets {evaluate(card)}.")
                else:
                    print(f"{self}'s other card is hidden.")

    def get_points(self):
        global tens
        tens = {'a', 'b', 'c', 'd'}         # set "tens" covers 10, J, Q, K, all of which also cause trouble being evaluated as ints
        for card in self.hand:
            if int(card[0], 16) < 10:
                self.points += int(card[0])
            elif card[0] in tens:
                self.points += 10
            else:                           # Ace
                self.points += 11
        if self.points == 21:
            print(f"\n{self} gets a Blackjack!")
            return True
        if self.is_dealer == False:
            print(f"\n{self} has {self.points} points.")
        else:
            global showing_points
            showing_points = self.hand[0][0] 
            if showing_points in tens:
                print(f"{self} has 10 points showing.")
                showing_points = 10
                return showing_points
            elif showing_points == 'e':
                print(f"{self} has 11 points showing.")
                showing_points = 11
                return showing_points
            else:
                print(f"{self} has {showing_points} points showing.")
                showing_points = int(showing_points)
                return showing_points

    def hit(self):
        if self.is_dealer:
            while self.points <= 16:
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
                if self.value_check():
                    return True
            self.stand = True
            print(f"{self} stands.")
        else:
            answers = "yn"
            prompt = input("Hit? (y/n) ")
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
                prompt = input("Hit again? (y/n) ")
                prompt = prompt.lower()
                while prompt not in answers:
                    prompt = input("Answer [Y]es or [N]o. ")
                if prompt == 'n':
                    break
                else:
                    continue
            self.stand = True
            print(f"{self} stands.")
    
    def value_check(self):
        if self.points == 21:
            print(f"{self} gets 21!")
            print(f"{self} wins!")
            return True
        elif self.points > 21:
            print(f"{self} goes bust!")
            return True

    def reveal(self, player):
        hidden_card = self.hand[0]
        print(f"{self} had {evaluate(hidden_card)}.")
        print(f"{self} had {self.points} points.")
        if self.points > player.points:
            print(f"{self} wins!")
        elif player.points > self.points:
            print("Player wins!")
        else:
            print("A tie! No one wins...")

def play_again(player1, player2):
    global game
    prompt = input("Play again? (y/n) ")
    while prompt.lower() != "n" and prompt.lower() != "y":
        prompt = input("Choose [Y] or [N]. ")
    if prompt.lower() == "y":
        player1.points = 0
        player2.points = 0
        global deck
        if len(deck) < 10:
            print("\nReshuffling...")
            shuffle()
        game = True
    else:
        game = False
        print("Goodbye.")

def shuffle():
    global deck
    deck = set()
    for i in range(13):
        deck.add(hex(i+2)[2:] + "S")
        deck.add(hex(i+2)[2:] + "H")
        deck.add(hex(i+2)[2:] + "D")
        deck.add(hex(i+2)[2:] + "C")
    return deck

def get_length():
    global deck
    print(f"There are {len(deck)} cards left in the deck.")


def evaluate(card):
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

def menu():
    global game
    prompt = input("[N]ew game or [Q]uit? ")
    while prompt.lower() != "n" and prompt.lower() != "q":
        prompt = input("Choose [N] or [Q]. ")
    if prompt.lower() == "n":
        game = True
    else:
        game = False
        print("Goodbye.")

def main():
    player = Player("Player")                       # create players
    dealer = Player("Dealer", is_dealer=True)       #
    shuffle()                                       # create deck
    menu()                                          # play or quit
    while game:
        get_length()
        player.deal()                               # deal cards
        dealer.deal()
        if not player.get_points():
            dealer.get_points()
        if not dealer.get_points():
            player.hit()
        if not player.hit():
            dealer.hit()
        if player.stand and dealer.stand:           # card reveal only if both players stand
            dealer.reveal(player)
        play_again(player, dealer)

main()
# menu()
# player = Player("Player")                       # create players
# dealer = Player("Dealer", is_dealer=True)       #
# shuffle()       
# while game:
#     print(f"There are {len(deck)} cards left in the deck.")
#     player.deal()                               # deal cards
#     dealer.deal()
#     play_again(player, dealer)