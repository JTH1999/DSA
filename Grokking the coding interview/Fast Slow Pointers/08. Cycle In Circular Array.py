# Cycle in a Circular Array 

# We are given an array containing positive and negative numbers. 
# Suppose the array contains a number ‘M’ at a particular index. 
# Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. 
# You should assume that the array is circular which means two things:

# If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
# If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.

# Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

# Example 1:
# Input: [1, 2, -1, 2, 2]
# Output: true
# Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

# Example 2:
# Input: [2, 2, -1, 2]
# Output: true
# Explanation: The array has a cycle among indices: 1 -> 3 -> 1

# Example 3:
# Input: [2, 1, -1, -2]
# Output: false
# Explanation: The array does not have any cycle.

def find_cycle(arr):
    length = len(arr)
    for i in range(length):
        if has_cycle(i, arr, length):
            return True
    
    return False

def has_cycle(i, arr, length):
    fast, slow = i, i
    isForward = True if arr[i] >= 0 else False 

    while fast != slow:
        slow = next_index(slow)
        fast = next_index(fast)

        if slow == -1 or fast == -1:
            return False

        fast = next_index(fast)

        if fast == -1:
            return False

    return True

def next_index(index, arr, length, isForward):
    if arr[index] >= 0 != isForward:
        return -1

    nextIndex = (index + arr[index]) % length:
    if nextIndex == index:
        return -1

    return nextIndex

# Time Complexity
# The above algorithm will have a time complexity of O(N^2) where ‘N’ is the 
# number of elements in the array. This complexity is due to the fact that we 
# are iterating all elements of the array and trying to find a cycle for each element.

# Space Complexity
# The algorithm runs in constant space O(1).

# An Alternate Approach
# In our algorithm, we don’t keep a record of all the numbers that have been 
# evaluated for cycles. We know that all such numbers will not produce a cycle 
# for any other instance as well. If we can remember all the numbers that have 
# been visited, our algorithm will improve to O(N) as, then, each number will 
# be evaluated for cycles only once. We can keep track of this by creating a 
# separate array however the space complexity of our algorithm will increase to O(N).


        