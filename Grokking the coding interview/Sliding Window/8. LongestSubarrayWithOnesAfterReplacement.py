# Leetcode 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/description/

# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

# Example 1:
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

# Example 2:
# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

def length_of_longest_substring(arr, k):
    windowStart = 0
    maxOnes = 0
    maxLength = 0
    
    for windowEnd in range(len(arr)):
        if arr[windowEnd] == 1:
            maxOnes += 1
            
        if windowEnd - windowStart + 1 - maxOnes > k:
            if arr[windowStart] == 1:
                maxOnes -= 1
            
            windowStart += 1
            
        maxLength = max(maxLength, windowEnd - windowStart + 1)
        
    return maxLength
    
# Time complexity O(N)
# Space complexity O(1)