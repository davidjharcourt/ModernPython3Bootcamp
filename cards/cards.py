import random

class Card:
    suit_allowed = ['Hearts','Diamonds','Clubs','Spades']
    value_allowed = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    
    def __init__(self, suit, value):
        if suit not in Card.suit_allowed:
            raise ValueError(f"You can't have a {suit} suit!")
        if value not in Card.value_allowed:
            raise ValueError(f"You can't have a {value} value!")
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
class Deck:   
    cards = [[x,y] for x in Card.suit_allowed for y in Card.value_allowed]
    def __init__(self):        
        self.cards = Deck.cards
        
    def count(self):
        return len(self.cards)
           
    def __repr__(self):
        return f"Deck of {self.count()} Cards"
    
    def _deal(self,num):
        if num <= self.count():
            hand = self.cards[-num:]
            del self.cards[-num:]
            return hand
        else:
            raise ValueError(f"All cards have been dealt")
    
    def shuffle(self):
        
        random.shuffle(self.cards)
        return self.cards
          
    def deal_card(self):
        return list(self._deal(1)[0])
    
    def deal_hand(self,num):
        return self._deal(num)
    
        
my_deck = Deck()
print(my_deck.count())
print(my_deck.__repr__())
#print(my_deck._deal(3))
print(my_deck.shuffle())
print(my_deck.deal_card())
print(my_deck.deal_hand(5))