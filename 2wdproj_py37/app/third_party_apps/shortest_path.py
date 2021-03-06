# from itertools import permutations
# from math import *
# from networkx.classes.filters import show_nodes
import numpy as np
import networkx as nx
# from numpy import testing
# import sys
from python_tsp.exact import solve_tsp_dynamic_programming


# Calculate path weight between two nodes
def path_cost(G, path):
    return sum([G[path[i]][path[i+1]]['weight'] for i in range(len(path)-1)])


def simulate_travel_path(G, visit):
    temp_Graph = nx.Graph()
    temp_Graph.add_nodes_from(visit)
    c = list(temp_Graph.nodes)
    for n in range(len(c)):
        for n1 in range(len(c)):
            if n == n1:
                continue
            try:
                if not temp_Graph.has_edge(c[n], c[n1]):
                    # print(c[n], c[n1])
                    cool_dist = list(nx.dijkstra_path(G, c[n], c[n1])) # Shortest path between c[n] & c[n1] using Dijkstra's Algo
                    # print(cool_dist)
                    total_weight = path_cost(G, cool_dist)
                    # print(total_weight)
                    temp_Graph.add_edge(c[n], c[n1], weight=total_weight)
            except Exception as e:
                print(e)
    return temp_Graph


def script_checkpt(
    warehouse_edges,
    warehouse_endpoint_edges,
    myArray
):
    print('\nwarehouse_edges:\n')
    for item in warehouse_edges:
        print(
            item
        )

    print(
        "\n\nwarehouse_endpoint_edges:",
        warehouse_endpoint_edges,
        "\n"
    )

    # print(
    #     "\n\nmyArray:",
    #     myArray,
    #     "\n"
    # )


# My array of nodes, columns A, B, C are present for now
warehouse_col = [
    'A',
    'B', 'C',
    'D', 'E',
    'F', 'G',
    'H', 'I',
    'J', 'K',
    'L'
]
warehouse_edges = []
warehouse_endpoint_edges = []
myArray = np.array(['Start'])

# Automatically adding the nodes A0 to C0,
for col in warehouse_col:
    # Number of rows in each warehouse column
    for num in range(0, 14):
        location = col + str(num)
        if num == 0:
            # Linking the start position to starting point of each warehouse
            # column E.g. A0, B0, C0 etc...
            warehouse_edges.append([myArray[0], location])
            warehouse_endpoint_edges.append(location)

# script_checkpt(warehouse_edges, warehouse_endpoint_edges, myArray)

        myArray = np.append(myArray, location)
        array_length = len(myArray)

        if num > 0:
            # Linking each node in each column to each other E.g. A0 -> A1, A1
            # -> A2
            warehouse_edges.append([myArray[array_length-2], location])
        if num == 13:
            warehouse_endpoint_edges.append(location)

# script_checkpt(warehouse_edges, warehouse_endpoint_edges, myArray)

# Link up columns B & C E.g. B0 -> C0, B1 -> C1 ... B10 -> C10
for nodes in myArray:
    if nodes[0] == 'B':
        hack = 'C' + nodes[1:]
        warehouse_edges.append([nodes, hack])
    elif nodes[0] == 'D':
        hack = 'E' + nodes[1:]
        warehouse_edges.append([nodes, hack])
    elif nodes[0] == 'F':
        hack = 'G' + nodes[1:]
        warehouse_edges.append([nodes, hack])
    elif nodes[0] == 'H':
        hack = 'I' + nodes[1:]
        warehouse_edges.append([nodes, hack])
    elif nodes[0] == 'J':
        hack = 'K' + nodes[1:]
        warehouse_edges.append([nodes, hack])

# script_checkpt(warehouse_edges, warehouse_endpoint_edges, myArray)

# Link the edges of warehouse col E.g. A0 -> B0, A10 -> B10, B0 -> C0, B10 ->
# C10
for idx in range(len(warehouse_endpoint_edges)):
    if idx + 2 < len(warehouse_endpoint_edges):
        warehouse_edges.append(
            [
                warehouse_endpoint_edges[idx],
                warehouse_endpoint_edges[idx+2]
            ]
        )

# script_checkpt(warehouse_edges, warehouse_endpoint_edges, myArray)

set_dist = 0
# Giving a weight to each edges
for edges in warehouse_edges:
    if(edges[0] == 'Start'):
        set_dist += 3
        edges.append(set_dist)
        continue
    weight = 2
    edges.append(weight)

# script_checkpt(warehouse_edges, warehouse_endpoint_edges, myArray)

# networkX
myGraph = nx.Graph()
# Adding nodes stored in the array to the graph
myGraph.add_nodes_from(myArray)
# myGraph.add_edges_from(warehouse_edges)  #This is the non-weighted function
myGraph.add_weighted_edges_from(warehouse_edges)
# print("Graph adjacency list: ")
# print(myGraph.adj)

# print("\n\nList of nodes in the graph: ")
# print(list(myGraph.nodes))

# So now add nodes are interconnected
# We only want to go to a few particular nodes so..
# Under the assumption there will always be a custom point of 'Start'
travel_log = [
    'Start', 'A7', 'A11', 'B2', 'C6', 'D3',
    'D9', 'E12', 'F2', 'H10', 'J8', 'L12'
]

# uh = simulate_edges_add_tsp(myGraph)
# Nodes in travel_log are points one wishes to travel to.
# Using simulate_travel_path, the weights are 
travel_Graph = simulate_travel_path(myGraph, travel_log)
# print(travel_Graph.edges(), sep='\n')

# print("\n\n")
b = nx.to_numpy_matrix(travel_Graph)
# Displaying the adjancency matrix
# print("The adjancency matrix: ")
# print(b)

permutation, distance = solve_tsp_dynamic_programming(b)
the_way = []
for n in range(len(permutation)):
    the_way.append(travel_log[permutation[n]])

print("\nThis is the shortest path to take: ")
print(the_way)
