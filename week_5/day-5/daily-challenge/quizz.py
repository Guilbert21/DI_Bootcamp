# PART 1
# q1 A Python class is like an outline for creating a new object
# q2 it is an object of a class 
# q3 it is binding of data and code acting on the methods to gether as a single unit 
# q4 a process of handling complexity by hiding unnecessary information from the user 
# q5 it is deriving a class from more than one direct base class
# q7 methods in the child class that have the same name as the methods in the parent class
# q8 is a set of rules that construct the linearization. In the Python literature, the idiom "the MRO of C" is also used as a synonymous for the linearization of the class C.

# PART 2

import random

class Card:
    def __init__(self,suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()
        
deck = Deck()
deck.shuffle()

for i in range(8):
    card = deck.deal()
    if card:
        print(card)
    else:
        print("no cards in the deck")
        break