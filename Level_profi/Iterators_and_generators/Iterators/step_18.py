class CardDeck:
    nominee = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    mast = ['пик', 'треф', 'бубен', 'червей']
    
    def __init__(self):
        self.index = 0
        

    def __iter__(self):
        return self
    
    def __next__ (self):
        if self.index >= 52:
            raise StopIteration

        mast = int(self.index/13)
        nomine = self.index%13
        card = self.nominee[nomine] + " " + self.mast[mast]
        self.index += 1

        return card
    

cards = list(CardDeck())

print(*cards)

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])