import os, sys
import numpy as np
from pprint import pprint
from collections import deque

delta_x = [-1, 1, 0, 0]
delta_y = [0, 0, 1, -1]

def q1(uni):
    exp_uni = expand(uni)
    pprint(exp_uni)
    return ""

def expand(uni):
    np_uni = np.array(uni)
    exp_uni  = np.array(uni)

    col_arr = np.empty((len(exp_uni)), dtype='str')
    col_arr[:] = '.'
    
    for i in range(0, len(np_uni[0])):
        col = np_uni[:,i]
        if np.all(col == '.'):
            exp_uni = np.insert(exp_uni, i + (len(exp_uni[0]) - len(np_uni[0])), [col_arr], axis= 1)

    row_arr = np.empty((len(exp_uni[0])), dtype='str')
    row_arr[:] = '.'
    
    for i in range(0, len(np_uni)):
        row = np_uni[i]
        if np.all(row == '.'):
            exp_uni = np.insert(exp_uni, i + (len(exp_uni) - len(np_uni)), [row_arr], axis= 0)
    
    return exp_uni

# def bfs():


#     def valid(x, y, uni):
#         if x < 0 or x >= len(uni) or y < 0 or y >= len(uni[x]):
#             return False
#         return (uni[x][y] != 1)

#     def solve(start, end):
#         Q = deque([start])
#         dist = {start: 0}
#         while len(Q):
#             curPoint = Q.popleft()
#             curDist = dist[curPoint]
#             if curPoint == end:
#                 return curDist
#             for dx, dy in zip(delta_x, delta_y):
#                 nextPoint = (curPoint[0] + dx, curPoint[1] + dy)
#                 if not valid(nextPoint[0], nextPoint[1]) or nextPoint in dist.keys():
#                     continue
#                 dist[nextPoint] = curDist + 1
#                 Q.append(nextPoint)

#     print(solve((0,0), (6,7)))


with open(os.path.join(sys.path[0], "input_test.txt"), "r") as file: 
    uni = [] 
    for i, line in enumerate(file.readlines()):  
        uni.append([*line.strip()])
    q1(uni)