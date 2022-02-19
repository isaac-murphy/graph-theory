#python 
''' implementation of several algoritms for graph exploration in python. For use with the Graph object 
in the related Graphs module. 
currently implemented: Bellman-Ford shortest path, Dijkstra shortest path
TODO: depth-first search, topological sort'''

import math
import heapq

def get_path(distances, pointers, end):
    if isinstance(pointers[end], type(None)): 
        return str(end) + '(' + str(distances[end]) + ')'
    else: 
        return get_path (distances, pointers, pointers[end]) + '-> ' + str(end) + ' (' + str(distances[end]) + ')'

def bellman_ford(G, s):
    distances = dict()
    pointers = dict()
    for node in G.S:
        if node == s:
            distances[node] = 0
            pointers[node] = None
        else: 
            distances[node] = math.inf
            pointers[node] = None
    N = len(G.S)
    for i in range(1, N):
        for (start, end), weight in G.w.items():
            if distances[end] > distances[start]+weight:
                    distances[end] = distances[start] + weight
                    pointers[end] = start
    
    return distances, pointers

def dijkstra(G, s):
    distances = dict()
    pointers = dict()
    for node in G.S:
        if node == s:
            distances[node] = 0
            pointers[node] = None
        else: 
            distances[node] = math.inf
            pointers[node] = None
    F = []
    for (node, dist) in distances.items():
        F.append((dist, node))
    #print(F)
    heapq.heapify(F) #heap 
    while F:
        dist, u = heapq.heappop(F)
        for v in G.A[u]:
            if distances[v] > distances[u]+G.w[(u, v)]:
                    distances[v] = distances[u] + G.w[(u, v)]
                    pointers[v] = u  
    return distances, pointers      

