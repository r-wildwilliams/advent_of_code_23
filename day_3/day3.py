import re

# Open input file
engine = []
file = open("input.txt")
for line in file:
    engine.append(line.strip())

# matrix check
for row in range(0, len(engine[:1])):
    for col in range(0, len(engine[row])):
        if engine[row][col].isdigit():
            ...