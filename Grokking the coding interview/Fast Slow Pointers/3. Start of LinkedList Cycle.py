# Start of linkedlist cycle

# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

class Node: 
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def find_cycle_start(head):
    # We first find the point where fast and slow pointer meet within the cycle
    # Then calculate the length of the cycle, k
    # Then set two pointers to head, move one ahead k steps.
    # Iterate both pointers until they meet - meet node will be start of cycle
    # Because one has walked k steps more, which is the cycle length

    fast, slow = head
    cycleLength = 0
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            cycleLength = find_cycle_length(slow)
            break

    fast, slow = head
    while cycleLength > 0:
        fast = fast.next
        cycleLength -= 1
    
    while fast != slow:
        fast = fast.next
        slow = slow.next

    return slow


def find_cycle_length(node):
    start = node
    count = 1

    while node.next != start:
        node = node.next
        count += 1

    return count

# Time complexity O(N)
# Space complexity O(1)