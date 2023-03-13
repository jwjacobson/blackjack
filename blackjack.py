#!/usr/bin/python
"""
What separates blackjack from other games
is that it's based on dependent events,
meaning past affects the probability in the future.
- William Tell, The Card Counter
"""

class Player:
    def __init__(self, stand=False, wins=0, points=0, is_dealer=False):
        self.wins = 0
        self.points = 0
        self.hand = list
        self.is_dealer = is_dealer
        self.stand = stand

    def win(self):
        self.wins += 1
        self.play_again()

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
                    print("The dealer's other card is hidden.")

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
            print(f"\nBlackjack!")
            self.win()
        if self.is_dealer == False:
            print(f"\nYou have {self.points} points.")
        else:
            if self.hand[0][0] in tens:
                print("The dealer has 10 points showing.")
            elif self.hand[0][0] == 'e':
                print("The dealer has 11 points showing.")
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
            else:
                self.stand = True
                print("The dealer stands.")
        else:
            answers = "yn"
            prompt = input("Hit? (y/n) ")
            prompt = prompt.lower()
            while prompt not in answers:
                prompt = input("Answer [Y]es or [N]o. ")
            if prompt == "y":
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
            else:
                self.stand = True
                print("You stand.")
    

    def hit_results(self):
        evaluate(new_card)
        print(f"The {self} gets the {value} of {suit}.")
        if self.points == 21:
            print("The {self} gets 21!")
            print("The {self} wins...")
            self.win()
        elif self.points > 21:
            print("The dealer goes bust!")
            print("You win!")
            player.win()
        
                # evaluate(new_card)
                # print(f"You get the {value} of {suit}.")
                # if self.points == 21:
                #     print("You get 21! You win!")
                #     self.win()
                # elif self.points > 21:
                #     print("You go bust! The dealer wins...")
                #     dealer.win()
                # else:
                #     print(f"You have {self.points} points.")
                #     prompt = input("Hit again? y/n ")
                #     while prompt not in answers:
                #         prompt = input("Answer [Y]es or [N]o. ")
                #     if prompt.lower() == "n":
                #         self.stand = True
                #         print("You stand.")
            
    def play_again(self):
        global game
        prompt = input("Play again? (y/n) ")
        while prompt.lower() != "n" and prompt.lower() != "y":
            prompt = input("Choose [Y] or [N]. ")
        if prompt.lower() == "y":
            self.points = 0
            game = True
        else:
            game = False
            print("Goodbye.")

    def reveal(self):
        evaluate(self.hand[0])
        print(f"The dealer had the {value} of {suit}.")
        print(f"The dealer had {self.points} points.")
        if self.points > Player.points:
            print("The dealer wins!")
            self.win()
        elif player.points > self.points:
            print("You win!")
            player.win()
        else:
            print("A tie! No one wins...")
            player.play_again()

def shuffle():
    global deck
    deck = set()
    for i in range(13):
        deck.add(hex(i+2)[2:] + "S")
        deck.add(hex(i+2)[2:] + "H")
        deck.add(hex(i+2)[2:] + "D")
        deck.add(hex(i+2)[2:] + "C")
    return deck

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
    player = Player()                   # create players
    dealer = Player(is_dealer=True)
    shuffle()                           # create deck
    menu()                                  
    while game:
        print(f"There are {len(deck)} cards left in the deck.")
        player.deal()                       # deal cards
        dealer.deal()
        player.get_points()                 # calculate point value of dealt cards
        dealer.get_points()
        player.hit()                        # user input function: allow hitting until bust
        dealer.hit()
        if player.stand and dealer.stand:   # card reveal only if both players stand
            dealer.reveal()
# main()

player = Player()                   
dealer = Player(is_dealer=True)
shuffle()
# player.deal()
# player.hit()
dealer.deal()
dealer.hit()

# dealer.win()
# print(dealer.wins)