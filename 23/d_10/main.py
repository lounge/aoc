import os, sys

maze = []

dirs = {
    'u': [0,-1],
    'r': [+1,0],
    'd': [0,+1],
    'l': [-1,0]
}

conns = {
    '|': [['u','d'], ['u','d']],
    '-': [['r','l'], ['r','l']],
    '7': [['u','r'], ['d','l']],
    'F': [['u','l'], ['r','d']],
    'J': [['d','r'], ['u','l']],
    'L': [['d','l'], ['u','r']],
    'S': [['u','r','d','l'],['u','r','d','l']],
    '.': [[]],
}

def q1():
    score = 0;
    curr = get_start();
    maze_loc = ''
    from_dir = ''

    while maze_loc != 'S':
        for dir in [x for x in dirs if x != from_dir]:
            curr_dir = dirs[dir]
            maze_loc = 'S' if maze_loc == '' else maze_loc

            if dir in conns[maze[curr[1] + curr_dir[1]][curr[0] + curr_dir[0]]][0] and dir in conns[maze_loc][1]:
                from_dir = list(dirs)[list(dirs).index(dir)-2]
                curr = [x + y for x, y in zip(curr, curr_dir)]
                maze_loc = maze[curr[1]][curr[0]]
                score = score + 1
                break

    return score/2

def get_start():
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if(char == 'S'):
                return [x, y];

with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    for i, line in enumerate(file.readlines()):        
        maze.append([*line.strip()])
    print(q1());