from collections import deque

# Breadth first search of adjacency matrix
# Returns path traversed
def bfs(graph: list[list[int]], source: int, needle: int) -> list[int]:
    seen = [False for i in range(len(graph))]
    prev = [-1 for i in range(len(graph))]

    seen[source] = True
    queue = deque()
    queue.append(source)

    # emulate do while loop
    # if condition at the end is the same as having the while condition at the end
    while True:
        current = queue.popleft()
        if current == needle:
            break

        adjs = graph[current]

        for i in range(len(adjs)):
            if adjs[i] == 0:
                continue
                
            if seen[i]:
                continue

            seen[i] = True
            prev[i] = current
            queue.append(i)

        if len(queue):
            break

    # build it backwards
    current = needle
    out = []

    while prev[current] != -1:
        out.append(current)
        current = prev[current]

    if len(out):
        # need to append the source as it has no parent so prev value is -1
        out.append(source)
        return out.reverse()
    
    return out





