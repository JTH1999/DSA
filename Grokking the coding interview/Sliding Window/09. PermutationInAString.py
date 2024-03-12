# https://leetcode.com/problems/permutation-in-string/
# Leetcode 567. Permutation in String

# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters it will have n! permutations.

# Example 1:

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.
# Example 3:

# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
# Example 4:

# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.

# My inital version

def find_permutation(str, pattern):
    windowStart = 0
    result = False
    frequencyHash = {}    
    patternHash = {}
    
    for index in range(len(pattern)):
        char = pattern[index]
        if char not in patternHash:
            patternHash[char] = 0
        patternHash[char] += 1
        
    for windowEnd in range(len(str)):
        rightChar = str[windowEnd]
        if rightChar not in frequencyHash:
            frequencyHash[rightChar] = 0
        frequencyHash[rightChar] += 1
        
        if windowEnd >= len(pattern) - 1:
            if frequencyHash == patternHash:
                result = True
                break
            leftChar = str[windowStart]
            frequencyHash[leftChar] -= 1
            if frequencyHash[leftChar] == 0:
                del frequencyHash[leftChar]
                
            windowStart += 1
            
    return result

# Improved version

def find_permutation(str, pattern):
    windowStart = 0
    result = False
    frequencyHash = {}    
    patternHash = {}
    
    for index in range(len(pattern)):
        char = pattern[index]
        if char not in patternHash:
            patternHash[char] = 0
        patternHash[char] += 1
        
    for windowEnd in range(len(str)):
        rightChar = str[windowEnd]
        if rightChar not in frequencyHash:
            frequencyHash[rightChar] = 0
        frequencyHash[rightChar] += 1
        
        if windowEnd >= len(pattern) - 1:
            if frequencyHash == patternHash:
                result = True
                break
            leftChar = str[windowStart]
            frequencyHash[leftChar] -= 1
            if frequencyHash[leftChar] == 0:
                del frequencyHash[leftChar]
                
            windowStart += 1
            
    return result

# Time complexity O(N + M) where N and M are numbers of characters in string and pattern respectively
# Space complexity O(M) since in the worst case the whole pattern can have distinct characters which will go into the hash map