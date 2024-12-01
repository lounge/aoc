import os, sys, re

score1 = 0
cards = []

def q1(card):
    score = 0;
    for i, v in enumerate(card):
       score = 1 if i == 0 else (score := score * 2)      
    return score

def q2():
    for i, card in enumerate(cards):
        for c in card:
            for x in range(c):
                if i+x+1 >= len(cards): break
                cards[i+x+1] += [cards[i+x+1][0]]

    return len([x for c in cards for x in c])

with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    for i, line in enumerate(file.readlines()):
        winning, acctual = line.split(":")[1].split("|");
        card = list(set(re.findall(r'\d+', winning)) & set(re.findall(r'\d+', acctual)))
        score1 += q1(card)
        cards.append([len(card)])
    
print(score1) 
print(q2())
