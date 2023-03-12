#!/usr/bin/python
"""
What separates blackjack from other games
is that it's based on dependent events,
meaning past affects the probability in the future.
- William Tell, The Card Counter
"""

class Player:
    def __init__(self, wins=0, points=0, is_dealer=False):
        self.wins = 0
        self.points = 0
        self.hand = list
        self.is_dealer = is_dealer
        self.stand = bool

    def deal(self):
        self.hand = []
        for i in range(2):
            self.hand.append(deck.pop())
        for card in self.hand:
            evaluate(card)
            if self.is_dealer == False:
                print(f"You get the {value} of {suit}.")
            else:
                if card == self.hand[0]:
                    print(f"The dealer gets the {value} of {suit}.")
                else:
                    print("The dealer's other card is hidden!")

    def get_points(self):
        global tens
        tens = {'a', 'b', 'c', 'd'}
        for card in self.hand:
            if int(card[0], 16) < 10:
                self.points += int(card[0])
            elif card[0] in tens:
                self.points += 10
            else:
                self.points += 11
        if self.points == 21:
            print(f"\nBlackjack!")
            self.wins += 1
            menu()
        if self.is_dealer == False:
            print(f"\nYou have {self.points} points.")
        else:
            print(f"The dealer has {self.hand[0][0]} points showing.")

    def hit(self):
        if self.is_dealer:
            if self.points <= 16:
                self.hand.append(deck.pop())
                new_card = self.hand[-1]
                if int(new_card[0], 16) < 10:
                    self.points += int(new_card[0])
                elif new_card[0] in tens:
                    self.points += 10
                else:
                    if self.points < 11:
                        self.points += 11
                    else:
                        self.points += 1
                evaluate(new_card)
                print(f"The dealer gets the {value} of {suit}.")
                if self.points == 21:
                    print("The dealer gets 21!")
                    print("The dealer wins...")
                elif self.points > 21:
                    print("The dealer goes bust!")
                    print("You win!")
            else:
                self.stand = True
                print("The dealer stands.")
        else:
            answers = "yn"
            prompt = input("Hit? (y/n) ")
            prompt = prompt.lower()
            while prompt not in answers:
                prompt = input("Answer [Y]es or [N]o. ")
            while prompt == "y":
                self.hand.append(deck.pop())
                new_card = self.hand[-1]
                if int(new_card[0], 16) < 10:
                    self.points += int(new_card[0])
                elif new_card[0] in tens:
                    self.points += 10
                else:
                    if self.points < 11:
                        self.points += 11
                    else:
                        self.points += 1
                evaluate(new_card)
                print(f"You get the {value} of {suit}.")
                if self.points == 21:
                    print("You get 21! You win!")
                    self.wins += 1
                    break
                elif self.points > 21:
                    print("You go bust! The dealer wins...")
                    break
                else:
                    print(f"You have {self.points} points.")
            else:
                self.stand = True
                print("You stand.")
            
    def reveal():
        pass

class Game():
    def __init__(self):
        pass

def shuffle():
    global deck
    deck = set()
    for i in range(13):
        deck.add(hex(i+2)[2:] + "S")
        deck.add(hex(i+2)[2:] + "H")
        deck.add(hex(i+2)[2:] + "D")
        deck.add(hex(i+2)[2:] + "C")

def evaluate(card):
    global value
    global suit
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
    menu()
    if game:
        print("\n")
        player = Player()
        dealer = Player(is_dealer=True)
        shuffle()
        player.deal()
        dealer.deal()
        player.get_points()
        dealer.get_points()
        player.hit()
        dealer.hit()
        # reveal()

main()