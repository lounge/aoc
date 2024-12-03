import os, sys, re

def check_diffs(diffs):
    return all([-3 <= d < 0 for d in diffs]) or all([0 < d <= 3 for d in diffs])

def q1(diff):
    if check_diffs(diff):
        return 1
    
    return 0

def q2(diff):
    if not check_diffs(diff):
        for i in range(len(report)):
            fixed = diff.copy()
            if i == 0:   
                fixed.pop(0)
            elif i == len(report)-1: 
                fixed.pop(-1)
            else:             
                d = fixed[i-1] + fixed.pop(i)    
                fixed[i-1] = d # += fixed.pop(i)
                # fixed.pop(i-1)

            if check_diffs(fixed):
                return 1
    
    return 0


with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    score1, score2 = 0, 0

    while line := file.readline():
        d = re.findall(r"\d+", line.strip())

        report = list(map(int, d))
        diffs = [a-b for a, b in zip(report[0::], report[1::])]

        score1 += q1(diffs)
        score2 += q2(diffs)

    print(score1)
    print(score1 + score2)


