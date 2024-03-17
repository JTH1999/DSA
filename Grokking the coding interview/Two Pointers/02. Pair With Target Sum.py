# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Example 1:

# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
# Example 2:

# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

def pair_with_target_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            return [left, right]
        
        if sum < target:
            left += 1
        else:
            right -= 1
        
    return [-1, -1]

# Time complexity O(N)
# Space complexity O(1)

# ALTERNATIVE APPROACH - WOULD WORK FOR UNSORTED ARRAY

def pair_with_targetsum(arr, target):
    nums = {}
    for i, num in enumerate(arr):
        if target - num in nums:
            return [i, nums[target - num]]
        else:
            nums[num] = i
    
    return [-1, 1]

# Time complexity O(N)
# Space complexity O(N) as worst case we will be pushing N items to hash table
