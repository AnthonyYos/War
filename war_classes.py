import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Card object creation and appended into the list
                new_card = Card(suit,rank)
                self.all_cards.append(new_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player():
    
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):

        # Type check to see if the we're adding one card or multiple cards
        # If type(new_card) is that of a list it means we're adding a list of cards due to a war situation
        # Extend adds each element within the new_cards list into all_cards as individual elements
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} cards"


# Test statments for deck class
# -------------------------------------------------------------
# new_deck = Deck()
# for x in new_deck.all_cards:
#     print(x)
# print(new_deck.all_cards[0])
# print(new_deck.deal_one())

# Test statements for player class
# -------------------------------------------------------------
# p1 = Player("Jeff")
# print(p1)
# p1.add_cards(new_deck.all_cards[0])
# print(p1)
