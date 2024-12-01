import os, sys, math

instr = ""
nodes = {}
dir = "LR"

def q1():
    turns = 0
    curr_node = "AAA"
    i = 0
    while curr_node != "ZZZ":
        i = 0 if i == len(instr) else i
        curr_node = nodes[curr_node][dir.index(instr[i])]
        i+=1
        turns+=1
    return turns

def q2(curr_nodes):
    node_turns = []
    for curr_node in curr_nodes:
        turns = 0
        i = 0
        while curr_node[-1] != "Z":
            i = 0 if i == len(instr) else i
            curr_node = nodes[curr_node][dir.index(instr[i])]
            i+=1
            turns+=1
        node_turns.append(turns)
    return math.lcm(*node_turns)

with open(os.path.join(sys.path[0], "input_01.txt"), "r") as file:  
    lines = file.read().splitlines()
    instr = lines.pop(0);
    for node in list(filter(None, lines)):
        n = node.split("=")
        nodes[n[0].strip()] = n[1].replace(" ", "").replace("(","").replace(")","").split(",")
    
    start_pos = list({key:value for key,value in nodes.items() if key[-1] == "A"}.keys())

    print(q1())
    print(q2(start_pos))