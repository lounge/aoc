import os
import sys
import re

def generate_combinations(answer, ops, q2 = False):
    results = set()
    n = len(ops)
    
    dp = [set() for _ in range(n + 1)]
    dp[0].add(0)
    
    for i in range(n):
        a = ops[i]
        for value in dp[i]:
            if value + a <= answer:
                dp[i + 1].add(value + a)
            if value * a <= answer:
                dp[i + 1].add(value * a)
            if q2 and int(f"{value}{a}") <= answer:
                dp[i + 1].add(int(f"{value}{a}"))
    
    return answer if answer in dp[n] else 0

def q1(answer, ops):
    return generate_combinations(answer, ops)

def q2(answer, ops):
    return generate_combinations(answer, ops, True)

with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:
    score1, score2 = 0, 0 
    lines = file.readlines()
    for line in lines:
        lists = line.strip().split(":")
        answer = int(re.findall(r"\d+", lists[0])[0])
        ops = [int(item) for item in re.findall(r"\d+", lists[1])]
 
        score1 += q1(answer, ops)                      
        score2 += q2(answer, ops)                      

print(score1)
print(score2)

    