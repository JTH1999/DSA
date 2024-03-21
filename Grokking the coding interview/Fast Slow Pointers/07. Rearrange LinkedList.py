# Rearrange a LinkedList
# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

# Example 1:
# Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
# Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 

# Example 2:
# Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
# Output: 2 -> 10 -> 4 -> 8 -> 6 -> null

def reorder(head):
    # Find middle node
    # Reverse second half
    # step through both, inserting second half nodes alternatively

    middle = find_middle(head)
    reversedSecondHalf = reverse(middle)

    p1, p2 = head, reversedSecondHalf

    while p1 != None and p2 != none:
        temp = p1.next
        p1.next = p2
        p1 = temp

        temp = p2.next
        p2.next = p1
        p2 = temp

    if p1 != None:
        p1.next = None

    return head


def find_middle(head):
    fast, slow = head

    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next

    return slow

def reverse(head):
    prev = None

    while head != None:
        next = head.next
        head.next = prev
        prev = head
        head = next
        
    return prev

# Time complexity O(N)
# Space complexity O(1)