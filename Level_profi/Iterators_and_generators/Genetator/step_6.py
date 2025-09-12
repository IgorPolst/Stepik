def card_deck(suit):
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    card_mastes = ["пик", "треф", "бубен", "червей"]
    card_number = 0
    while True:
        
        card_value = card_values[card_number%13]
        card_mast = card_mastes[int(card_number/13%4)]
        card_number +=1
        if(suit == card_mast):
            continue
        yield f"{card_value} {card_mast}"

generator = card_deck('пик')

print(next(generator))
print(next(generator))
print(next(generator))