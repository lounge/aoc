import os, sys, re

def check_order(update, up_rules):
    for rule in up_rules:
        idx = update.index(rule[0])
        idx2 = update.index(rule[1])

        if idx > idx2:
            return False
        else:
            continue

    return True

def sort_update(update, up_rules):   
    for rule in up_rules:        
        idx = update.index(rule[0])
        idx2 = update.index(rule[1])

        if idx > idx2:
            update[idx], update[idx2] = update[idx2], update[idx]
            sort_update(update, up_rules)
        else:
            continue
 

def q1(update, up_rules):
    if check_order(update, up_rules):
        return int(update[int((len(update) - 1) / 2)])
    return 0

def q2(update, up_rules):
    if not check_order(update, up_rules):
        sort_update(update, up_rules)
        return int(update[int((len(update) - 1) / 2)])
    return 0


with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    
    rules, updates = [], []
    score1, score2 = 0, 0

    while line := file.readline():
        nums = re.findall(r"\d+", line.strip())
        if "|" in line:
            rules.append(nums)
        elif "," in line:
            updates.append(nums)

    
    for idx, update in enumerate(updates):  
        up_rules = []
        for rule in rules:
            if all(r in update for r in rule):
                up_rules.append(rule)
        
        score1 += q1(update, up_rules)
        score2 += q2(update, up_rules)                        

    print(score1)
    print(score2)




