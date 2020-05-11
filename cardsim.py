import random

class Card:
    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def __init__(self, suitInput, rankInput):
        self.suit = suitInput
        self.rank = rankInput

class Deck:
    def shuffle(self):
        self.deck = random.sample(self.deck, len(self.deck))
        
    def draw(self):
        if (len(self.deck) > 0):
            return self.deck.pop()
        else:
            return None
    
    def __init__(self):
        self.deck = []   
        for x in range (4):
            for y in range (13):
                self.deck.insert(0,Card(x, y))
            
def main():
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    deck1 = Deck()

    for x in range (0, 52):
        drawncard = deck1.draw()
        print (ranks[drawncard.getRank()], " of ", suits[drawncard.getSuit()])

    print ("\nShuffling the cards... \n")
    
    deck1 = Deck()
    
    deck1.shuffle()
    
    for x in range (0, 52):
        drawncard = deck1.draw()
        print (ranks[drawncard.getRank()], " of ", suits[drawncard.getSuit()])
main()
