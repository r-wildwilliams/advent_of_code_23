# Open input file
with open("/Users/reilly.wildwilliams/Documents/advent_of_code/day_2/input.txt", "r") as file:
    games = file.read().splitlines()

### PART 1
# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?
example_pull = {"red": 12, "green": 13, "blue": 14}

def parse_game(game: str) -> dict:
    split = game.split(":")
    
    # Get Game ID
    id = split[0].replace('Game ', '')

    # Get Subsets
    subsets = split[1].replace(' ', '').split(";")
    runs = []
    for subset in subsets:
        # Green
        if subset.find("green") != -1: # if a green marble was pulled
            if subset[subset.find("green")-2].isdigit(): # two digit number
                green = int(subset[subset.find("green")-2:subset.find("green")])
            elif subset[subset.find("green")-1].isdigit(): # one digit number
                green = int(subset[subset.find("green")-1])
            else:
                raise ValueError("Unsupported marble count. Counts must be integers", subset[subset.find("green")-1:subset.find("green")+6])
        else:
            green = 0     

        # Red
        if subset.find("red") != -1: # if a red marble was pulled
            if subset[subset.find("red")-2].isdigit():
                red = int(subset[subset.find("red")-2:subset.find("red")])
            elif subset[subset.find("red")-1].isdigit(): # one digit number
                red = int(subset[subset.find("red")-1])
            else:
                raise ValueError("Unsupported marble count. Counts must be integers", subset)
        else:
            red = 0

        # Blue
        if subset.find("blue") != -1: # if a blue marble was pulled
            if subset[subset.find("blue")-2].isdigit():
                blue = int(subset[subset.find("blue")-2:subset.find("blue")])
            elif subset[subset.find("blue")-1].isdigit(): # one digit number
                blue = int(subset[subset.find("blue")-1])
            else:
                raise ValueError("Unsupported marble count. Counts must be integers", subset[subset.find("blue")-1:subset.find("blue")+6])
        else:
            blue = 0

        runs.append({"blue": blue, "green": green, "red": red})

    return {"ID": id, "subsets": runs, "raw": game}

def ball_count(game: dict) -> int:
    max_balls = 0
    for run in game["subsets"]:
        balls = run["blue"] + run["green"] + run["red"]
        if balls > max_balls:
            max_balls = balls
    return max_balls

def color_maxes(game: dict) -> dict:
    red = 0
    green = 0
    blue = 0
    for run in game["subsets"]:
        if run["red"] > red:
            red = run["red"]
        if run["green"] > green:
            green = run["green"]
        if run["blue"] > blue:
            blue = run["blue"]
    return {"red": red, "green": green, "blue": blue}

# GO THROUGH GAMES
values = 0
for game in games:
    parsed = parse_game(game)

    # check if max balls is more than example pull
    max_balls = ball_count(parsed)
    if max_balls <= example_pull["green"] + example_pull["red"] + example_pull["blue"]: # possible games only
        colors = color_maxes(parsed)
        if colors["green"] <= example_pull["green"]:
            if colors["red"] <= example_pull["red"]:
                if colors["blue"] <= example_pull["blue"]:
                    values += int(parsed["ID"])
    
print("PART 1 SOLUTION: ", values)

### PART 2
# what is the fewest number of cubes of each color that could have been in 
# the bag to make the game possible?

def fewest_cubes(game: dict) -> int:
    parsed = parse_game(game)
    red = None
    green = None
    blue = None
    for run in parsed["subsets"]:
        if red is not None:
            if run["red"] > red:
                red = run["red"]
        else:
            red = run["red"]

        if green is not None:
            if run["green"] > green:
                green = run["green"]
        else:
            green = run["green"]

        
        if blue is not None:
            if run["blue"] > blue:
                blue = run["blue"]
        else:
            blue = run["blue"]

    parsed["fewest"] = {"red": red, "blue": blue, "green": green}
    return parsed

# GO THROUGH GAMES
powers = 0
for game in games:
    fewest = fewest_cubes(game)["fewest"]
    powers += fewest["red"] * fewest["blue"] * fewest["green"]

print("PART 2 SOLUTION: ", powers)
