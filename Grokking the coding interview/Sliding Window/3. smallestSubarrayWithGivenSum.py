# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
# https://glucko.github.io/codeprep/GrokkCode/2._Pattern_Sliding_Window/3._Smallest_Subarray_with_a_given_sum_(easy)/1.2_Smallest_Subarray_with_a_given_sum_(easy)_-.html

def smallest_sub_array_with_given_sum(s, arr):
    smallestLength = len(arr) + 1
    windowStart, windowSum = 0, 0
    
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        
        while windowSum >= s:
            smallestLength = min(smallestLength, windowEnd + 1 - windowStart)
            windowSum -= arr[windowStart]
            windowStart += 1
        
    if smallestLength = len(arr) + 1:
        smallestLength = 0
        
    return smallestLength
    
# Time complexity O(N)
# Space complexity O(1)