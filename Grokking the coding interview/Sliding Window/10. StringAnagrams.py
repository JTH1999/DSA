# Given a string and a pattern, find all anagrams of the pattern in the given string.

# Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

# abc
# acb
# bac
# bca
# cab
# cba
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

# Example 1:
# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

# Example 2:
# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

def find_string_anagrams(str, pattern):
    windowStart = 0
    anagrams = []
    frequencyHash = {}    
    patternHash = {}
    
    for char in range(len(pattern)):
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
                anagrams.append(windowStart)
            leftChar = str[windowStart].
            frequencyHash[leftChar] -= 1
            if frequencyHash[leftChar] == 0:
                del frequencyHash[leftChar]
                
            windowStart += 1
            
    return anagrams
    
# Time Complexity #
# The time complexity of the above algorithm will be O(N+M) where ‘N’ and ‘M’ 
# are the number of characters in the input string and the pattern respectively.

# Space Complexity #
# The space complexity of the algorithm is O(M) since in the worst case, the whole 
# pattern can have distinct characters which will go into the HashMap. In the worst case, 
# we also need O(N) space for the result list, this will happen when the pattern has only 
# one character and the string contains only that character.