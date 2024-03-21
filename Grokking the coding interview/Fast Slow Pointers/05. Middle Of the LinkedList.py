# Middle of the LinkedList

# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

# If the total number of nodes in the LinkedList is even, return the second middle node.

# Example 1:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3

# Example 2:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Output: 4

# Example 3:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
# Output: 4

def find_middle(head):
    fast, slow = head

    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next

    return slow

# Time complexity O(N)
# Space complexity O(1)