# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Given a string, find the length of the longest substring which has no repeating characters.

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".

def non_repeat_substring(str):
    longest = 0
    windowStart = 0
    characterIndexMap = {} # Contains last index of each character as we loop through the string.
    
    for windowEnd in range(len(str)):
        rightChar = str[windowEnd]
        
        if rightChar in characterIndexMap:
            # If right character already in our window, we set windowStart to the next index along
            # If windowStart is already ahead of our last rightChar index, it stays as is.
            windowStart = max(windowStart, characterIndexMap[rightChar] + 1)
        
        characterIndexMap[rightChar] = windowEnd
            
        longest = max(windowEnd - windowStart + 1, longest)
        
    return longest
    
# I initially solved this using a frequency hashmap similar to the Longest Substring with K Distinct Characters problem, but this index hashmap approach
# is faster because it removes the need for the while loop. Same overall time complexity, but in practice this algorithm will be twice as fast as its O(N) rather than O(N+N)

# Time complextiy O(N)
# Space complexity O(K), where K is the number of distinct characters in the string. Worst case, K <= N, since each character in the string could be distinct.