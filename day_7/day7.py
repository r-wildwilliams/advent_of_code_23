### POKER
import copy

example = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

with open("input.txt", "r") as file:
    data = file.read()

data = data.strip().splitlines()

# RULES
def label_hands(hands: []) -> dict[dict]:
    hand_labels = {}
    for hand in hands:
        hand_labels[hand] = {}
        cards, bet = hand.split(" ")
        
        unique_cards = {}
        for card in cards:
            if card not in unique_cards.keys():
                unique_cards[card] = 1
            else:
                unique_cards[card] += 1
        
        pairs = []
        for card, count in unique_cards.items():
            if count == 5:
                hand_labels[hand] = {"label": "five_of_a_kind", "cards": cards, "bid": bet}
            elif count == 4:
                hand_labels[hand] = {"label": "four_of_a_kind", "cards": cards, "bid": bet}
            elif count == 3:
                hand_labels[hand] = {"label": "three_of_a_kind", "cards": cards, "bid": bet}
            elif count == 2 and card not in pairs:
                pairs.append(card)
        if len(pairs) > 1:
            hand_labels[hand] = {"label": "two_pair", "cards": cards, "bid": bet}
        elif len(pairs) == 1:
            if hand_labels[hand] == {}:
                hand_labels[hand] = {"label": "one_pair", "cards": cards, "bid": bet}
            else:
                hand_labels[hand] = {"label": "full_house", "cards": cards, "bid": bet}
        elif  hand_labels[hand] == {}:
            hand_labels[hand] = {"label": "high_card", "cards": cards, "bid": bet}
    return hand_labels

def rank_labels(hand_labels: dict):
    sorter = {"five_of_a_kind": [], "four_of_a_kind": [], "full_house": [], "three_of_a_kind": [], "two_pair": [], "one_pair": [], "high_card": []}
    card_ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    # create ranking list for later processing
    ranks = copy.deepcopy(sorter)
    for rank in ranks:
        ranks[rank].extend([] for i in range(0, len(card_ranks)))
    
    # split hands into labels
    for key, details in hand_labels.items():
        for rank in sorter:
            if details["label"] == rank:
                sorter[rank].append(key)

    
    alphabet = ""
    for elem in card_ranks:
        alphabet += elem
    
    # sort hands within each label
    for rank in sorter:
        ranks[rank] = sorted(sorter[rank], key=lambda word: [alphabet.index(c) for c in word.split(" ")[0]])

    # unpack ranks and assing a rank to each hand
    rank = len(hand_labels.keys())
    ranked = {}
    for label in ranks:
        for item in ranks[label]:
            ranked[item] = rank
            rank -= 1
    
    return ranked

def total_winnings(ranked: dict) -> int:
    total_winnings = 0
    for hand, rank in ranked.items():
        bid = int(hand.split(" ")[1])
        total_winnings += rank*bid
    return total_winnings

# ## PART 1
hand_labels = label_hands(data)
ranked = rank_labels(hand_labels)
print("PART 1 SOLUTION: ", total_winnings(ranked))
