# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.

# Example 2:
# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.

def search_triplets(arr):
    arr.sort()
    triplets = []
    
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_pairs(arr, -arr[i], i + 1, triplets) # we pass in left because we have already found all triplets involving elements to the left of i at this point
        
    return triplets
    
    
def search_pairs(arr, target, left, triplets):
    right = len(arr) - 1
    
    while left < right:
        leftNum = arr[Left]
        rightNum = arr[right]
        sum = leftNum + rightNum
        if sum == target:
            triplets.append([leftNum, rightNum, -target])
            left += 1
            right -= 1
            
            # Skip duplicates
            while left < right && arr[left] == arr[left - 1]:
                left += 1
            while left < right && arr[right] == arr[right + 1]:
                right -= 1
        elif sum < target:
            leftNum += 1
        else: 
            rightNum -= 1
            
    return [-1, -1]
    
# Time Complexity 
# Sorting array takes O(NlogN)
# Search pair takes O(N)
# We call O(N) N times, so overall complexity is O(NlogN + N^2) which is asymptotically equivalent to O(N^2)

# Space complexity
# Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.

# Solution Explanation
# This problem follows the Two Pointers pattern and shares similarities with Pair with Target Sum. A couple of differences are that
# the input array is not sorted and instead of a pair we need to find triplets with a target sum of zero.

# To follow a similar approach, first, we will sort the array and then iterate through it taking one number at a time. Let’s say
# during our iteration we are at number ‘X’, so we need to find ‘Y’ and ‘Z’ such that X+Y+Z==0. At this stage, our problem
# translates into finding a pair whose sum is equal to “−X” (as from the above equation Y+Z==−X).

# Another difference from Pair with Target Sum is that we need to find all the unique triplets. To handle this, we have to
# skip any duplicate number. Since we will be sorting the array, so all the duplicate numbers will be next to each other and are easier to skip.