import random

class Card:
    def __init__(self, rank = 0, suit = ""):
        try:
            if rank.upper() == "A":
                rank = 1
            elif rank.upper() == "Q":
                rank = 12
            elif rank.upper() == "K":
                rank = 13
            elif rank.upper() == "J":
                rank = 11
            self.rank = rank
        except:
            self.rank = rank
    
        try:
            self.suit = suit.upper()
        except:
            self.suit = suit

        


    def __str__(self):
        list_of_numbers = [1, 11, 12 ,13]
        list_of_royals = ["A","J", "Q", "K"]
        if self.suit in ["H", "S", "D", "C"] and  (1 <= self.rank <= 13) :
            if self.rank in list_of_numbers:
                self.rank = list_of_royals[list_of_numbers.index(self.rank)]
            return "{:>3}".format(str(self.rank) + self.suit.upper())
        else:
            return  "{:>3}".format("blk")

    def is_blank(self):
        if Card(self.rank, self.suit) == "blk":
            return True
        else:
            return False 
    




class Deck:
    def __init__(self):
        self.deck = []
        self.rank = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
        self.suit = ["S","H","D","C"]
        for ranks in self.rank:
            for suits in self.suit:
                self.deck.append(str(ranks)+ suits)

    def __str__(self):
        self.returning_string = ""
        for index, card in enumerate(self.deck):          
            if index % 13 == 0 and index != 0:
                self.returning_string += "\n"
            self.returning_string += " {:>3s}".format(card)
        return self.returning_string
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop(0)

class PlayingHand:
    
    def __init__(self):
        self.hand = []
        self.NUMBERCARDS = 13 
        for cards in range(self.NUMBERCARDS):
            self.hand.append("blk")
            
    
    def __str__(self):
        return " ".join(self.hand)
            
    def add_card(self, card):
        for index, the_card in enumerate(self.hand):
            if the_card == "blk":
                self.hand[index] = card
                break
            
            
        


def test_cards():
    card1 = Card()
    print(card1)
    card2 = Card(5,'s')
    print(card2)
    card3 = Card('Q','D')
    print(card3)
    card4 = Card('x', 7)
    print(card4)

def print_4_hands(hand1, hand2, hand3, hand4):
    ''' Prints the 4 hands '''
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)

def deal_4_hands(deck, hand1, hand2, hand3, hand4):
    ''' Deals cards for 4 hands '''
    PlayingHand.NUMBER_CARDS = 13
    for i in range(PlayingHand.NUMBER_CARDS):
        hand1.add_card(deck.deal())
        hand2.add_card(deck.deal())
        hand3.add_card(deck.deal())
        hand4.add_card(deck.deal())

def test_hands(deck):
    hand1 = PlayingHand()
    hand2 = PlayingHand()
    hand3 = PlayingHand()
    hand4 = PlayingHand()
    print("The 4 hands:")
    print_4_hands(hand1, hand2, hand3, hand4)

    deal_4_hands(deck, hand1, hand2, hand3, hand4)
    print("The 4 hands after dealing:")
    print_4_hands(hand1, hand2, hand3, hand4)

# The main program starts here
random.seed(10)
test_cards()

deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)

test_hands(deck)
print("The deck after dealing:")
print(deck)
        
    
