# 340. Longest substring with at most K distinct characters (premium)
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

# Given a string, find the length of the longest substring in it with no more than K distinct characters.
# https://glucko.github.io/codeprep/GrokkCode/2._Pattern_Sliding_Window/4._Longest_Substring_with_K_Distinct_Characters_(medium)/1.2_Longest_Substring_with_K_Distinct_Characters_(medium)_-.html

def longest_substring_with_k_distinct_characters(k, str):
    length = 0
    windowStart = 0
    charFrequency = {}
    
    for windowEnd in range(len(str)):
        rightChar = str[windowEnd]
        if rightChar not in charFrequency:
            charFrequency[rightChar] = 0

        charFrequency[rightChar] += 1
        
        # Shrink the sliding window until we have k distinct characters in charFrequency
        while len(charFrequency) > k:
            leftChar = str[windowStart]
            charFrequency[leftChar] -= 1 # decrememnt the character frequency
            
            if charFrequency[leftChar] == 0: # remove from the hashmap if frequency is 0
                del charFrequency[leftChar]
            
            windowStart += 1 # shrink the window
        
        length = max(windowEnd - windowStart + 1, length)
    
    return length
    
# Time complexity O(N) - outer loop runs for all character, inner while loop runs for each character only once, so time is O(N+N) = O(N)
# Space complexity O(K) - storing a maximum of k+1 characters in the hashmap