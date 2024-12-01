import os, sys, re

l1 = []
l2 = []
def q1():
    score = 0
    for i in range(len(l1)):
        score += abs(l1[i]-l2[i])
    return score


def q2():
    score = 0
    for i in range(len(l1)):
       score += l1[i] * l2.count(l1[i])
    return score


with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    while line := file.readline().rstrip():
        d = re.findall(r"\d+", line.rstrip())
        l1.append(int(d[0]))
        l2.append(int(d[1]))

    l1.sort()
    l2.sort()
    print(q1())
    print(q2())
