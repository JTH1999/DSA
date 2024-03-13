# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

# Example 1:
# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

# Example 2:
# Input: [-3, -1, 1, 2], target=1
# Output: 0
# Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

# Example 3:
# Input: [1, 0, 1, 1], target=100
# Output: 3
# Explanation: The triplet [1, 1, 1] has the closest sum to the target.

def search_triplet(arr, target):
    arr.sort()
    smallestDifference = inf
    
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            sum = arr[left] + arr[right] + arr[i]
            if sum == target:
                return target
            
            difference = target - sum
            smallestDifference = difference if abs(difference) < abs(smallestDifference) else smallestDifference
            
            if sum > target:
                right -= 1
            else:
                left += 1
    
    return target - difference
    
# Time Complexity 
# Sorting O(NlogN)
# For each element, we loop through each element again, so overall time complexity is O(NlogN + N^2) which is 
# equivalent asymptotically to O(N^2)

# Space Complexity - O(N) for the sorting