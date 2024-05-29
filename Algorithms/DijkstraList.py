from Algorithms.AdjacencyListDFS import GraphEdge
import math

def hasUnvisited(seen: list[bool], dists: list[int]) -> bool:
    has = False
    
    for i in range(len(seen)):
        if not seen[i] and dists[i] < math.inf:
            has = True

    return has

def getLowestUnvisited(seen: list[bool], dists: list[int]) -> int:
    lowestDistance = math.inf
    index = -1

    for i in range(len(dists)):

        if seen[i]:
            continue

        if dists[i] < lowestDistance:
            lowestDistance = dists[i]
            index = i
    
    return index
        


def dijkstra_list(source: int, sink: int, arr: list[list[GraphEdge]]) -> list[int]:
    seen = [False for i in range(len(arr))]
    dists = [math.inf for i in range(len(arr))]
    prev = [-1 for i in range(len(arr))]

    dists[source] = 0

    # Could use a min heap here instead to improve time complexity
    while hasUnvisited(seen, dists):
        current = getLowestUnvisited(seen, dists)
        seen[current] = True

        adjs = arr[current]
        for i in range(len(adjs)):
            edge = adjs[i]
            if seen[edge.to]:
                continue
        
            dist = dists[current] + edge.weight
            if dist < dists[edge.to]:
                dists[edge.to] = dist
                prev[edge.to] = current

    out = []
    current = sink

    while prev[current] != -1:
        out.append(current)
        current = prev[current]

    out.append(source)
    return out.reverse()

