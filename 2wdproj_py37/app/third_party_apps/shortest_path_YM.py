# import numpy as np
import pandas as pd
from scipy.spatial import distance_matrix
from python_tsp.exact import solve_tsp_dynamic_programming

#       LEGEND
#     'Start': [18, 2],
#     'A': [4, 1],
#     'B': [8, 1],
#     'C': [13, 3],
#     'D': [9, 4],
#     'E': [5, 6],
#     'F': [12, 6],
#     'G': [3, 7],
#     'H': [13, 9],
#     'I': [5, 12],
#     'J': [7, 15],
#     'K': [3, 18]

testpts_coords = [
    [18, 2],
    [4, 1],
    [8, 1],
    [13, 3],
    [9, 4],
    [5, 6],
    [12, 6],
    [3, 7],
    [13, 9],
    [5, 12],
    [7, 15],
    [3, 18]
]

testpts_alphabets = [
    'Start',
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K'
]

df = pd.DataFrame(
    testpts_coords,
    columns=['xcoord', 'ycoord'],
    index=testpts_alphabets
)

dist_mat = pd.DataFrame(
    distance_matrix(df.values, df.values),
    index=df.index,
    columns=df.index
)

dist_mat_test = dist_mat
dist_mat = dist_mat.to_numpy()

permutation, distance = solve_tsp_dynamic_programming(dist_mat)

shortest_route = []
for each_pt in permutation:
    shortest_route.append(testpts_alphabets[each_pt])
print('\nShortest Route:', shortest_route)
print('Distance:', distance, '\n')

# Testing if indeed, that is the shortest distance computed
# proposed_route = [
#     'Start',
#     'A', 'B', 'C', 'D', 'E',
#     'F', 'G', 'H', 'I', 'J',
#     'K'
# ]
proposed_route = [
    'Start',
    'F', 'H', 'J', 'K', 'I',
    'G', 'E', 'A', 'B', 'D',
    'C'
]
dist = []
# for i in range(len(testpts_alphabets)):
for i in range(len(proposed_route)):
    try:
        dist.append(
            # dist_mat_test.loc[testpts_alphabets[i], testpts_alphabets[i+1]]
            dist_mat_test.loc[proposed_route[i], proposed_route[i+1]]
        )
    except IndexError:
        dist.append(
            # dist_mat_test.loc[testpts_alphabets[i], testpts_alphabets[0]]
            dist_mat_test.loc[proposed_route[i], proposed_route[0]]
        )

print('Testing: Distance Calculation of Proposed Route')
print('Proposed Route:', proposed_route)
print('Distance:', sum(dist), '\n')
