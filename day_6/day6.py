from functools import reduce

### EXAMPLE RACES
example = """
Time:      7  15   30
Distance:  9  40  200
"""

# HELPER FUNCTIONS
def get_winning_combos(races: list[dict]) -> list[dict]:
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
    return races

def get_product_combo_counts(races: list[dict]) -> int:
    combo_counts = []
    for race in races:
        combo_counts.append(len(race["winning_combos"]))
    return reduce((lambda x, y: x * y), combo_counts)

def basic_preprocessing(rawtext: str) -> list:
    return rawtext.strip().replace("Time: ","").replace("Distance: ","").strip().splitlines()

# PART 1
with open("input.txt", "r") as file:
    races = file.read()
races = basic_preprocessing(races)
raw = []
for i in races:
    raw.append([int(n) for n in list(filter(None, i.split(" ")))])
races = []
for i in range(0, len(raw[0])):
    races.append({"time": raw[0][i], "distance": raw[1][i]})

races = get_winning_combos(races)
total = get_product_combo_counts(races)
print("SOLUTION FOR PART 1: ", total)

# PART 2
with open("input.txt", "r") as file:
    races = file.read()

races = basic_preprocessing(races)
raw = []
for i in races:
    nums = [n for n in list(filter(None, i.split(" ")))]
    total = ''
    for num in nums:
        total = total + num
    total = int(total)
    raw.append(total)

races = [{"time": raw[0], "distance": raw[1]}] # convert to list for function input
races = get_winning_combos(races)
total = get_product_combo_counts(races)
print("SOLUTION FOR PART 2: ", total)
