# Open input file
with open("input.txt", "r") as file:
    cards = file.read().splitlines()

def numerize_list(lister: list[str]) -> list[int]:
    lister = list(filter(None, lister))
    lister = [int(elem) if elem.isnumeric else ValueError("Non-numeric list element: ", elem) for elem in lister]
    return lister

class Card:
    def __init__(self, card: str):
        self.raw = card
        self.ID = card[card.find(":")-1:card.find(":")]
        winners = card[card.find(":")+2:card.find("|")-1].split(" ")
        self.winners = numerize_list(winners)
        youhave = card[card.find("|")+2:len(card)].split(" ")
        self.youhave = numerize_list(youhave)
    def find_winners_in_hand(self):
        winning_numbers = []
        for num in self.youhave:
            if num in self.winners:
                winning_numbers.append(num)
        self.winning_numbers = winning_numbers
    def get_hand_total(self):
        if len(self.winning_numbers) > 0:
            self.hand_total = pow(2,len(self.winning_numbers)-1)
        else:
            self.hand_total = 0
    def get_copies(self):
       self.copies = list(range(int(self.ID), int(self.ID)+len(self.winning_numbers)+1))
        



# PART 1
points = 0
for card in cards:
    card_obj = Card(card)
    card_obj.find_winners_in_hand()
    card_obj.get_hand_total()
    points += card_obj.hand_total
    
print("PART 1 SOLUTION: ", points)

# PART 2
from collections import Counter
from itertools import chain

def flatten_chain(matrix):
    return list(chain.from_iterable(matrix))

cards = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

copies = []
for card in cards:
    copies = sum(copies, [])
    card_obj = Card(card)
    card_obj.find_winners_in_hand()
    card_obj.get_copies()
    print(card_obj.ID, card_obj.copies)
    counts = Counter(copies)
    print(counts)
    print(copies)
    if counts[card_obj.ID] > 0: # how many copies do we have?
        copies.append(card_obj.copies) * counts[card_obj.ID]
    else:
        copies.append(card_obj.copies)
    print(copies)

print(copies)


#     for elem in card_obj.copies:
#         card_copies.append(elem)

# counts = Counter(card_copies)
# print(counts)

