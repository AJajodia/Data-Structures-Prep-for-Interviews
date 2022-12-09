import random


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        if value == "Ace":
            self.points = 11
        elif value == "King" or value == "Queen" or value == "Jack":
            self.points = 10
        else:
            self.points = self.value
        if suit == "Hearts" or "Diamonds":
            self.color = "Red"
        else:
            self.color = "Black"

    def __repr__(self):
        return str(self.value) + " of " + self.suit


class Deck:
    def __init__(self):
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        self.suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        self.list = [Card(self.values[i], self.suits[j]) for i in range(13) for j in range(4)]


def turn(deck):
    total = 0
    firstcard = deck.list[random.randint(0, len(deck.list)-1)]

    total += firstcard.points
    deck.list.remove(firstcard)
    print(firstcard)
    print(total)
    while total < 21:
        card = deck.list[random.randint(0, len(deck.list)-1)]

        if input("Hit or stay? ") == "h":
            total += card.points
        else:
            print("You got " + str(total))
            return total
        print(card)
        deck.list.remove(card)
        print(total)
    print("You busted")
    return 0


def dealer(deck):
    total = 0
    firstcard = deck.list[random.randint(0, len(deck.list))]
    total += firstcard.points
    deck.list.remove(firstcard)
    print(firstcard)
    print(total)
    while total < 17:
        card = deck.list[random.randint(0, len(deck.list))]
        total += card.points
        print(card)
        deck.list.remove(card)
        print(total)
    if total > 21:
        print("Dealer busted")
        return 0
    else:
        print("Dealer has " + str(total))
        return total


def blackjack(playercount):
    deck = Deck()
    scores = {"Player " + str(j + 1): 0 for j in range(playercount)}
    print(scores)
    for i in scores:
        scores[i] = turn(deck)
    dealerscore = dealer(deck)
    for i in scores:
        if dealerscore <= scores[i]:
            print(i + " wins")
        else:
            print(str(dealerscore) + " > " + str(scores[i]))
            print(i + " loses")


blackjack(4)
