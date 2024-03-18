# Palindrome LinkedList
# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

# Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

# Example 1:
# Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
# Output: true

# Example 2:
# Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
# Output: false

def is_palindrome(head):
    # Find middle of linked list
    # reverse second half of list
    # check if first half equals second half
    # reverse second half again and attach it to first half

    # Find middle
    fast, slow = head

    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next

    headSecondHalf = reverse_list(slow)
    copy = headSecondHalf

    while (head != None and headSecondHalf != None):
        if head.value != headSecondHalf.value:
            break # Not a palindrome

        head = head.next
        headSecondHalf = headSecondHalf.next

        reverse_list(copy)

        if head == None or headSecondHalf == None: # Both halves match
            return True
        
        return False

def reverse_list(head):
    prev = None

    while head != None:
        next = head.next
        head.next = prev
        prev = head
        head = next
        
    return prev

# Time complexity O(N)
# Space complexity O(1)