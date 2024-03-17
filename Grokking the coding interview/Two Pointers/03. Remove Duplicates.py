# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

# Example 1:
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

# Example 2:
# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].

def remove_duplicates(arr):
    nextNonDuplicate = 1
    index = 1

    while index < len(arr):
        if arr[nextNonDuplicate - 1] != arr[index]:
            arr[nextNonDuplicate] = arr[index]
            nextNonDuplicate += 1
        index += 1

    return nextNonDuplicate

# Time Complexity 
# The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.

# Space Complexity
# The algorithm runs in constant space O(1).