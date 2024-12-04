import os, sys, re

word = ["X", "M", "A", "S"]
dirs = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

def get_char(x, y, grid):    
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return None
    return grid[y][x]

def check_dirs(x, y, dir, w):
    for i, char in enumerate(w[1::]):
        x += dir[0]
        y += dir[1]
        next_char = get_char(x, y, grid)
        if next_char != char:
            return 0
    return 1

def check_x_dirs(x, y, dir, w):
    first_char = get_char(x + dir[0], y + dir[1], grid)
    last_char = get_char(x + (dir[0] * -1), y + (dir[1] * -1), grid)
    if first_char == w[0] and last_char == w[-1]:
        return 1
    return 0

def q1(grid):
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "X":
                for dir in dirs:
                    score += check_dirs(x, y, dir, word)
    return score

def q2(grid):
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "A":
                x_val = 0
                for dir in dirs[::2]:
                    x_val += check_x_dirs(x, y, dir, word[1::])
                    if x_val == 2:
                        score += 1
                        break
    return score


with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    grid = []
    
    while line := file.readline():
        grid.append(list(line.strip()))

    print(q1(grid))
    print(q2(grid))




