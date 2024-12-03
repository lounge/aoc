import os, sys, re

def mult_fact(factors):
    return sum([int(x) * int(y) for x, y  in factors])

def get_factors(line):
    muls = re.findall(r"mul\(\d+,\d+\)", line.strip())
    return [(re.findall(r"\d+", m)) for m in muls]

def q1(factors):
    return mult_fact(factors)

def q2(line):
    pattern_to_remove = r"don't\(\).*?do\(\)"
    removes = re.findall(pattern_to_remove, line)
    for r in removes:
        line = line.replace(r, "")

    clean_line = line.split("don't()")[0]
    return mult_fact(get_factors(clean_line))

with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    big_line = ""
    while line := file.readline():
        big_line += line.replace("\n", "")

    print(q1(get_factors(big_line)))
    print(q2(big_line))




