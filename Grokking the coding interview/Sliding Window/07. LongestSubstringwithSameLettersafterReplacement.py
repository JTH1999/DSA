# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1
# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

# Example 2
# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

# Example 3
# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

# This solution took a while for me to wrap my head around how it works.
# My first thought was that this is just the longest substring with k+1 distinct characters. Which as I'm now writing I realise is completely wrong.
# That would work if you were replacing every instance of a distinct letter with a single replace, not individual letters.

# The key to this solution is that we don't really ever shrink the the window, it either grows or slides along.

def length_of_longest_substring(str, k):
    windowStart = 0
    maxLength = 0
    maxRepeatLetterCount = 0
    frequencyMap = {}
    
    for windowEnd in range(len(str)):
        rightChar = str[windowEnd]
        if rightChar not in frequencyMap:
            frequencyMap[rightChar] = 0
        frequencyMap[rightChar] += 1
        
        maxRepeatLetterCount = max(maxRepeatLetterCount, frequencyMap[rightChar])
        
        # Shift the window along if maxRepeatLetterCount has not increased - this is the key step
        if windowEnd - windowStart + 1 - maxRepeatLetterCount > k:
            leftChar = str[windowStart]
            frequencyMap[leftChar] -= 1
            if frequencyMap[leftChar] == 0:
                del frequencyMap[leftChar]
            
            windowStart += 1
            
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    
    return maxLength
    
# Time complexity O(N)
# Space complexity O(N)