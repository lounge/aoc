
import os, sys, re, math

matrix = []

def q1():
    score = 0

    for i, row in enumerate(matrix):
        matches = re.finditer(r'\d+', row)
        for m in matches:
            start =  m.start() if m.start() == 0 else m.start()-1;
            end = m.end()-1 if m.end() >= len(row) else m.end()

            search = []
            if i > 0:
                up = matrix[i-1][start:end+1]
                search.append(up)
            if i < len(matrix) -1:
                down = matrix[i+1][start:end+1]
                search.append(down)
            
            current = matrix[i][start:end+1]
            search.append(current)

            for s in search:
                regex = re.compile("[^0-9.]")
                if regex.search(s) != None:
                    score += int(m.group(0))
                    break
    return score;

def q2():
    score = 0
    part_list = []
    for i, row in enumerate(matrix):
        matches = re.finditer(r'\*', row)
        for m in matches:
            start =  m.start() if m.start() == 0 else m.start()-1;
            end = m.end()-1 if m.end() >= len(row) else m.end()

            search = []
            if i > 0:
                up = matrix[i-1]
                search.append(up)
            if i < len(matrix) -1:
                down = matrix[i+1]
                search.append(down)
            
            current = matrix[i]
            search.append(current)

            part_nums = []
            for s in search:
                regex = re.compile(r"\d+")
                numbers =regex.finditer(s)
                for n in numbers:
                    nEnd = n.end()-1;
                    if (nEnd in range(start, end)) or (n.start() in range(start, end+1)) or (n.start() <= start and nEnd >= end):
                        part_nums.append(int(n.group(0)))

            part_list.append(part_nums)

    for part in part_list:
        if len(part) == 2:
            score += math.prod(part)

    return score


with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    while (line := file.readline().rstrip()):
        matrix.append(line)
    
    print(q1())
    print(q2())


