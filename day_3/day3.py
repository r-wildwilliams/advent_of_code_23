import re

example = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# data = list(filter(None, example.splitlines()))

with open("input.txt", "r") as file:
    data = file.read()
data = list(filter(None, data.splitlines()))

# generate tuples of row to check plus row above and below
row_above_below = []
for n in range(0, len(data)):
    if n-1 > -1:
        if n+1 < len(data):
            row_above_below.append((data[n-1], data[n], data[n+1]))
        else:
            row_above_below.append((data[n-1], data[n], ''))
    else:
        row_above_below.append(('', data[n], data[n+1]))

def parts_symbols_before_after(target_row: str) -> list[int]:
    part_numbers = []
    symbol_after = re.findall(r'(\d+)([@#$%^&*()!])', target_row)
    if symbol_after:
        for couple in symbol_after:
            for obj in couple:
                if obj.isnumeric():
                    part_numbers.append(int(obj))


    symbol_before = re.findall(r'([@#$%^&*()!])(\d+)', target_row)
    if symbol_before:
        for couple in symbol_before:
            for obj in couple:
                if obj.isnumeric():
                    part_numbers.append(int(obj))

    return part_numbers


# check second item in tuple for each item in row_above_below (target row to check!)
part_numbers = []
for row_cluster in row_above_below:
    target_row = row_cluster[1]
    already_found = []

    # easy ones first: numbers with symbols directly before or after them: DONE!
    parts = parts_symbols_before_after(target_row)
    if parts:
        for part in parts:
            part_numbers.append(part)
            already_found.append(part) # keep list of what we've already got

    # hard ones now: numbers with symbols adjacent to them
    nums = re.findall(r'\d+', target_row)
    for num in nums:
        if num not in already_found: # filter out already found parts
            index_start = target_row.find(num)
            index_end = target_row.find(num)+len(num)

            # get valid search ranges
            if index_start-1 < 0:
                search_start = 0
                search_end = index_end+1
            elif index_end > len(target_row):
                search_end = index_end
                search_start = index_start-1
            else:
                search_start = index_start-1
                search_end = index_end+1

            # check rows above and below for adjacent symbols
            if re.findall(r'[^.\d]+', row_cluster[0][search_start:search_end]): # filter out non periods and digits in row above
                already_found.append(int(num))
                part_numbers.append(int(num))
            elif re.findall(r'[^.\d]+', row_cluster[2][search_start:search_end]): # filter out non periods and digits in row below
                already_found.append(int(num))
                part_numbers.append(int(num))

print("PART 1 SOLUTION: ", sum(part_numbers))

