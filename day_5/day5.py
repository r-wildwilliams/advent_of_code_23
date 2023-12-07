data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
with open('input.txt', 'r') as file:
    data = file.read()

# DATA PREPROCESSING
seeds = [int(i) for i in list(filter(None, data.split("\n")))[0].split(": ")[1].split(" ")]
raw = list(filter(None, data.replace("map:", "").split("\n")))[1:]
maps = {}
for index in range(0, len(raw)):
    if not raw[index][0].isnumeric():
        maps[raw[index].strip()] = []
        counter = 1
        while index+counter < len(raw) and raw[index+counter][0].isdigit():
            maps[raw[index].strip()].append([int(num) for num in raw[index+counter].split(" ")])
            counter += 1

# GET LOCATION FOR AN INPUT SEED
# def seed_to_location(seed: int, maps: dict) -> int: # uncomment for part 1
def seed_to_location(arguments) -> int: # comment out for part 1
    seed = arguments[0]
    maps = arguments[1][1]
    source = seed
    # loop through each map
    for map, specs in maps.items():
        done_specs = []
        for spec in specs:
            destination_range_start = spec[0]
            source_range_start = spec[1]
            range_length = spec[2]
            if source in range(source_range_start, source_range_start+range_length) and map.split("-")[2] not in done_specs:
                destination_index = list(range(source_range_start, source_range_start+range_length)).index(source)
                source = range(destination_range_start, destination_range_start+range_length)[destination_index]
                done_specs.append(map.split("-")[2])
    print(f"seed {seed} corresponds to location {source}")
    return source


# locations = []
# for seed in seeds:
#     location = seed_to_location(seed, maps)
#     print(f"Seed {seed} is located at {location}")
#     locations.append(location)

# print("PART 1 SOLUTION: ", min(locations)) # haha that was so inefficient

### PART 2
from copy import deepcopy
seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_range = range(seeds[i],seeds[i]+seeds[i+1])
    for seed in seed_range:
        seed_ranges.append(seed)

map_range = output = list((x, deepcopy(maps)) for x in seed_ranges)

# parallelize my previous solution
import multiprocessing as mp

if __name__ == '__main__':
    with mp.Pool(4) as p:
        results = p.map(seed_to_location, zip(seed_ranges, map_range))
        print(results)

    print(min(results))
