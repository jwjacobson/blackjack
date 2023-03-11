
class Player:
    pass

deck = set()
for i in range(13):
    deck.add(f"{i+1}s")
    deck.add(f"{i+1}h")
    deck.add(f"{i+1}d")
    deck.add(f"{i+1}c")

hand = []

def deal():
    for i in range(2):
        hand.append(deck.pop())
    print(hand)

deal()
print(len(deck))
