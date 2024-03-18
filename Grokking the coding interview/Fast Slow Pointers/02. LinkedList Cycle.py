# LinkedList Cycle

# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

class Node: 
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def has_cycle(head):
    # If there is a cycle, it is guaranteed that the fast pointer will equal the slow pointer 
    # at some point during the slow pointer's first loop of the cycle
    fast, slow = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True

    return False

# Time complexity O(N)
# Space complexity O(1)

# Similar problem: Given the head of a LinkedList with a cycle, find the length of the cycle

# Solution: find the point where fast and slow meet. Then from that point do a loop with 
# the slow pointer until it reaches the start point, counting each step.