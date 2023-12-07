import numpy as np
import re
from scipy.ndimage import convolve

with open("input.txt") as src:
    schematic = np.array([
        [*line.strip()]
        for line in src
    ])

### part one

nums = [*map(str, range(10))]


def make_viable_mask(num_mask, viability_init):    
    viable_mask = convolve(
        num_mask & viability_init,
        [[1, 1, 1]],
    ) & num_mask

    if (viable_mask == viability_init).all():
        return viable_mask

    return make_viable_mask(num_mask, viable_mask)

def get_viable_nums(schematic, viability_init):
    viability_init = convolve(
        viability_init,
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ],
    )
    num_mask = np.isin(schematic, nums)
    viable_mask = make_viable_mask(num_mask, viability_init)
    
    clean_schematic = np.full_like(schematic, " ")
    clean_schematic[viable_mask] = schematic[viable_mask]

    out = sum([
        re.split(r"\s+", "".join(line))
        for line in clean_schematic
    ], start=[])
    return [*map(int, filter(lambda x: x, out))]
    
symbol_mask = ~np.isin(schematic, nums+["."])
print("part one answer:", sum(get_viable_nums(schematic, symbol_mask)))

