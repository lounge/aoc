import os, sys, re

def q1(zip):
    return sum([abs(x - y) for x, y in zip])


def q2(l1, l2):
    return sum(x * l2.count(x) for x in l1)

with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    l1, l2 = [], []

    while line := file.readline():
        d = re.findall(r"\d+", line.strip())
        l1.append(int(d[0]))
        l2.append(int(d[1]))

    l1.sort()
    l2.sort()

    print(q1(zip(l1, l2)))
    print(q2(l1, l2))
