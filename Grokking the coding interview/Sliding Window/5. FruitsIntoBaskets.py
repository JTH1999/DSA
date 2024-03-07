# 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/description/

# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

def fruits_into_baskets(fruits):
    windowStart = 0
    fruitCounts = {}
    maxFruitCount = 0
    
    for windowEnd in range(len(fruits)):
        right = fruits[windowEnd]
        if right not in fruitCounts:
            fruitCounts[right] = 0
        fruitCounts[right] += 1
        
        while len(fruitCounts) > 2:
            left = fruits[windowStart]
            fruitCounts[left] -= 1
            if fruitCounts[left] == 0:
                del fruitCounts[left]
            windowStart += 1
            
        maxFruitCount = max(maxFruitCount, windowEnd - windowStart + 1)

    return maxFruitCount

# Time complexity O(N)
# Space complexity O(1) as there can be a maximum of three types of fruit stored in the frequency map