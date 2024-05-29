class GraphEdge:
    def __init__(self, to: int = None, weight: int = None) -> None:
        self.to = to
        self.weight = weight
        

def walk(graph: list[list[GraphEdge]], current: int, needle: int, seen: list[bool], path: list[int]) -> bool:
    if seen[current]:
        return False
    
    seen[current] = True
    
    # recurse
    # prev
    path.append(current)

    if current == needle:
        return True

    # recurse
    list = graph[current]
    for i in range(len(list)):
        edge = list[i]
        if walk(graph, edge.to, needle, seen, path):
            return True

    # post
    path.pop()

    return False

def dfs(graph: list[list[GraphEdge]], source: int, needle: int) -> list[int]:
    seen = [False for i in range(len(graph))]
    path = []

    walk(graph, source, needle, seen, path)

    return path

