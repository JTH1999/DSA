# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

# Example 1:
# Input: [-1, 0, 2, 3], target=3 
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

# Example 2:
# Input: [-1, 4, 2, 1, 3], target=5 
# Output: 4
# Explanation: There are four triplets whose sum is less than the target: 
#    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2): # Pay attention to the - 2 here!!! Don't forget it
        count += search_pairs(arr, target - arr[i], i + 1)

    return count

def search_pairs(arr, target, left):
    count = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] < target:
            # originally had count += 1 here, but we can say count += right - left since arr[right] will always be greater than arr[left]
            # so arr[left] + arr[right] is always less than target here
            # Time complexity would be N^3 using my inital approach!
            count += right - left
            left += 1
        else:
            right -= 1

    return count

# Time complexity O(N^2)
# Space complexity O(N) because sorting

# If this was changed to recording each triplet rather than the count, how would the time complexity change?

# Time complexity would go to N^3 because rather than the count += right - left step we need to iterate through 
# each item of the array from the right, for each increment of left. So search_pairs goes to O(N^2)
