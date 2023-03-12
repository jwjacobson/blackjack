#!/usr/bin/python
"""
What separates blackjack from other games
is that it's based on dependent events,
meaning past affects the probability in the future.
"""

class Player:
    def __init__(self, wins=0, losses=0, points=0, is_dealer=False):
        self.wins = 0
        self.losses = 0
        self.points = 0
        self.hand = list
        self.is_dealer= is_dealer

    def deal(self):
        self.hand = []
        for i in range(2):
            self.hand.append(deck.pop())
        for card in self.hand:
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
            if self.is_dealer == False:
                print(f"You get the {value} of {suit}.")
            else:
                if card == self.hand[0]:
                    print(f"The dealer gets the {value} of {suit}.")
                else:
                    print("The dealer's other card is hidden!")

    def get_points(self):
        tens = {'a', 'b', 'c', 'd'}
        for card in self.hand:
            if int(card[0], 16) < 10:
                self.points += int(card[0])
            elif card[0] in tens:
                self.points += 10
            else:
                self.points += 11
        if self.points == 21:
            print("\nBlackjack!")
            self.wins += 1
        if self.is_dealer == False:
            print(f"\nYou have {self.points} points.")
        else:
            print(f"The dealer has {self.hand[0][0]} points showing.")

        def hit(self):
            answers = "yn"
            prompt = input("Hit? (y/n) ")
            while prompt.lower() not in answers:
                prompt = input("Answer [Y]es or [N]o. ")
            




def shuffle():
    global deck
    deck = set()
    for i in range(13):
        deck.add(hex(i+2)[2:] + "S")
        deck.add(hex(i+2)[2:] + "H")
        deck.add(hex(i+2)[2:] + "D")
        deck.add(hex(i+2)[2:] + "C")




player = Player()
dealer = Player(is_dealer=True)
shuffle()
player.deal()
dealer.deal()
player.get_points()
dealer.get_points()