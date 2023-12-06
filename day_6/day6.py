### EXAMPLE RACES
example = """
Time:      7  15   30
Distance:  9  40  200
"""

with open("input.txt", "r") as file:
    races = file.read()

# PRE-PROCESSING
races = races.strip().replace("Time: ","").replace("Distance: ","").strip().splitlines()
raw = []
for i in races:
    raw.append([int(n) for n in list(filter(None, i.split(" ")))])
races = []
for i in range(0, len(raw[0])):
    races.append({"time": raw[0][i], "distance": raw[1][i]})

# PART 1
from functools import reduce

for race in races:
    hold = 0
    go = 0
    winning_combos = []
    while hold < race["time"]:
        hold += 1
        go = hold*(race["time"] - hold)
        if go > race["distance"]:
            winning_combos.append({"hold": hold, "go": go})

    race["winning_combos"] = winning_combos

combo_counts = []
for race in races:
    combo_counts.append(len(race["winning_combos"]))
total = reduce((lambda x, y: x * y), combo_counts)
print("SOLUTION FOR PART 1: ", total)

