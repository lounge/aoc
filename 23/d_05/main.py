import os, sys, math, re

def q1(clean_maps):

    almanac = [];

    for i, maps in enumerate(clean_maps):
        max_val = max([item for sublist in maps for item in sublist])
        almanac.append(list(range(0, max_val+1)))

        for map in maps:
            d, r = map[1], map[2]
            almanac[i] = 0
    



    return ""

with open(os.path.join(sys.path[0], "input_test.txt"), "r") as file:  
    # lines = file.read().splitlines()
    lines = [i for i in file.read().splitlines() if i]
    # os.linesep.join([s for s in file.splitlines() if s])
    seeds = re.findall(r'\d+', lines.pop(0))

    maps = []
    ranges = []
    for i, line in enumerate(lines):
        vals = re.findall(r'\d+', line)
        if len(vals) > 0:
            ranges.append([ int(x) for x in vals ]);
        else:
            maps.append(ranges)
            ranges = []
    maps.append(ranges)

    q1(maps[1:len(maps)+1])