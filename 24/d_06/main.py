import os, sys
import copy

dir = [(0, -1), (1, 0), (0, 1), (-1, 0)] # U R D L

def find_guard(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "^":
                return (x, y)

def modify_grid(grid_copy, x, y):
    if grid[y][x] == "." or grid[y][x] == "^":
        grid_copy[y][x] = "#"

def move(grid, start_pos, detect_loops=False):
    path, path_dir = set(), set()
    curr_dir = dir[0]
    x, y = start_pos

    while True:
        xm, ym = x + curr_dir[0], y + curr_dir[1]

        if detect_loops and (xm, ym, curr_dir) in path_dir:
            return len(path), 1
        if xm < 0 or xm >= len(grid[0])  or ym < 0 or ym >= len(grid):
            break
        if grid[ym][xm] == "#":
            curr_dir = dir[(dir.index(curr_dir) + 1) % 4]
            continue   
        else:
            x = xm
            y = ym
            path.add((x, y))
            path_dir.add((x, y, curr_dir))
    
    return len(path), 0

def q1(grid):
    score = move(grid, find_guard(grid))
    print(score)

def q2(grid):
    loops = 0
    guard = find_guard(grid)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid_copy = copy.deepcopy(grid)
            modify_grid(grid_copy, x, y)
            path, loop = move(grid_copy, guard, True)
            loops += loop     
    print(loops)

with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    grid = []

    while line := file.readline():
        grid.append(list(line.strip()))                           

    q1(grid)
    q2(grid)




