from collections import deque

def bfs(head, toFind):
    # We use a queue for breadth first search
    # deque is python queue implementation (double ended queue, can be used as queue or stack)
    # popLeft is dequeue, append is enqueue
    queue = deque()
    queue.append(head)

    while len(queue):
        current = queue.popleft()

        if current.value == toFind:
            return True

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return False