import os, sys, re

score1 = 0
hist = []

def q1(line):
    lines = []
    lines.append(line)

    while not all(v == 0 for v in line):
        line = [j-i for i, j in zip(line[:-1], line[1:])]
        lines.append(line)
    
    hist.append(lines)

    for rev_hist in hist:
        for i, l in enumerate(reversed(rev_hist)):
            if i == 0:
                l.append(0)
            else:
                a = rev_hist[len(rev_hist)-i-1][len(l)-1] 
                b = rev_hist[len(rev_hist)-i][len(l)-1]
                l.append(b+a)
                
    return hist[0][0][-1]

def q2(hist):
    for rev_hist in hist:
        for i, l in enumerate(reversed(rev_hist)):
            if i == 0:
                l.insert(0, 0)
            else:
                a = rev_hist[len(rev_hist)-i-1][0] 
                b = rev_hist[len(rev_hist)-i][0]
                l.insert(0, a-b)

    return sum(x[0][0] for x in hist)

with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    for i, line in enumerate(file.readlines()):
        score1 += q1([ int(x) for x in re.findall('-?\d+\.?\d*', line) ])
        
    print(score1)
    print(q2(hist))