from day7 import *

#Cases provided by LxsterGames
#https://www.reddit.com/r/adventofcode/comments/18cr4xr/2023_day_7_better_example_input_not_a_spoiler/
firstCase = ['JJJJJ 37',
             'AAAAA 61']

secondCase = ['Q2KJJ 13',
             'Q2Q2Q 19',
             'T3T3J 17']

thirdCase = ['2345A 1',
             'Q2KJJ 13',
             'Q2Q2Q 19',
             'T3T3J 17',
             'T3Q33 11',
             '2345J 3',
             'J345A 2',
             '32T3K 5',
             'T55J5 29',
             'KK677 7',
             'KTJJT 34',
             'QQQJA 31',
             'JJJJJ 37',
             'JAAAA 43',
             'AAAAJ 59',
             'AAAAA 61',
             '2AAAA 23',
             '2JJJJ 53',
             'JJJJ2 41']

TESTER = """
QQQQQ 115
QQQQK 101
QQQJJ 112
QQQJT 122
QQJJT 718
QQJT9 11
QJT98 4
"""

tester = TESTER.splitlines()


## TEST FIRST CASE
hand_labels = label_hands(thirdCase)
ranked = rank_labels(hand_labels)
for hand, rank in ranked.items():
    print(hand, rank)
print("THIRD CASE SOLUTION: ", total_winnings(ranked))
