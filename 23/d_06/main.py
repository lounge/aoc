import os, sys, math

def q1(chart):
    return math.prod(calc(chart))

def q2(chart):
    return calc(chart)[0]

def calc(chart):
    score = []
    for i, c in enumerate(chart):
        dist = int(chart[i][1])
        list = []
        for x in range(1, int(chart[i][0])):
            list.append(x * (int(chart[i][0]) - x))
        score.append(len([i for i in list if i > dist]))
    return score

with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    lines = file.readlines()
    print(q2([[''.join(map(str, lines[0].split(":")[1].split())), ''.join(map(str, lines[1].split(":")[1].split()))]]))
    print(q1(list(zip(lines[0].split(":")[1].split(), lines[1].split(":")[1].split()))))