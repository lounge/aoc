import os, sys, re, math

score1 = 0
score2 = 0
colors = ["red", "green", "blue"]

def q1(rounds, cubes, gameNr):
    game = parse_game(rounds)
    return gameNr if sum([int(i <= j) for i,j in zip(game, cubes)]) == 3 else 0

def q2(rounds):
    game = parse_game(rounds)
    return math.prod(game)

def parse_game(rounds):
    game = [0, 0, 0]

    for r in rounds:
        for d in r:
            for c in colors:
                if c in d:
                    idx = colors.index(c)
                    val = re.search(r'\d+', d).group(0);
                    if (game[idx] < int(val)):
                        game[idx] = int(val) 
    return game


with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    for i, line in enumerate(file.readlines()):
        lines = line.split(":")[1].split(";");
        rounds = [r.split(",") for r in lines if r]
        score1 += q1(rounds, [12, 13, 14], i+1)
        score2 += q2(rounds)

print(score1)
print(score2)