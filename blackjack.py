#!/usr/bin/python
"""
What separates blackjack from other games
is that it's based on dependent events,
meaning past affects the probability in the future.
"""

# class Player:
#     def __init__(self, )


deck = set()
for i in range(13):
    deck.add(hex(i+2)[2:] + "S")
    deck.add(hex(i+2)[2:] + "H")
    deck.add(hex(i+2)[2:] + "D")
    deck.add(hex(i+2)[2:] + "C")

hand = []

def deal():
    for i in range(2):
        hand.append(deck.pop())
    print(hand)
    for card in hand:
        if int(card[0], 16) < 10:
            value = card[0]
            # print(f"You got a {card[2]}")
        elif card[0] == "a":
            value = "10"
            # print("You got a 10.")
        elif card[0] == "b":
            value = "Jack"
            # print("You got a Jack.")
        elif card[0] == "c":
            value = "Queen"
            # print("You got a Queen.")
        elif card[0] == "d":
            value = "King"
            # print("You got a King.")
        else:
            value = "Ace"
            # print("You got an Ace.")
        if value:
            if card[1]  == "S":
                suit = "Spades"
            elif card[1]  == "H":
                suit = "Hearts"
            elif card[1]  == "D":
                suit = "Diamonds"
            elif card[1]  == "C":
                suit = "Clubs"
            else:
                print("error")
        if value == "8" or value == "Ace":
            print(f"You got an {value} of {suit}.")
        else:
            print(f"You got a {value} of {suit}.")
        
deal()