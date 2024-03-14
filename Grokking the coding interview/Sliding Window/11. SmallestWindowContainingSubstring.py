# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

# Example 1:
# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"

# Example 2:
# Input: String="abdabca", Pattern="abc"
# Output: "abc"
# Explanation: The smallest substring having all characters of the pattern is "abc".

# Example 3:
# Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.

def find_substring(str, pattern):
    windowStart = 0
    patternHash = {}
    minLength = len(str) + 1
    substringStart = 0
    matches = 0

    for char in pattern:
        if char not in patternHash:
            patternHash[char] = 0
        patternHash[char] += 1

    for windowEnd in range(len(str)):
        rightChar = str[windowEnd]
        if rightChar in patternHash:
            patternHash[rightChar] -= 1
            if patternHash[rightChar] == 0:
                matches += 1

    while matches == len(patternHash):
        windowLength = windowEnd - windowStart + 1
        if windowLength < minLength:
            minLength = windowLength
            substringStart = windowStart

        # shrink window
        leftChar = str[windowStart]
        if leftChar in patternHash:
            patternHash += 1
            if patternHash[leftChar] == 1:
                matches -= 1

        windowStart += 1

    if minLength > len(str):
        return ""
    
    return str[substringStart : substringStart + minLength]