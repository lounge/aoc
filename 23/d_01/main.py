import os, sys, re

numbers = ['one','two','three','four','five','six','seven','eight','nine']

score1 = 0
score2 = 0

def q1(line):
    m = re.findall(r"\d", line)
    return int(m[0] + m[-1])

def q2(line):
    p = re.compile("(?=(" + "|".join(numbers) + "|\d))")
    pe = p.findall(line)

    vals = [];
    for val in [pe[0], pe[-1]]:
        if val in numbers: 
            vals.append(str(numbers.index(val)+1))
        else: 
            vals.append(str(int(val)))
        
    return int(''.join(vals))

with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    while (line := file.readline().rstrip()):
        score1 += q1(line)
        score2 += q2(line)

print(score1)
print(score2)
