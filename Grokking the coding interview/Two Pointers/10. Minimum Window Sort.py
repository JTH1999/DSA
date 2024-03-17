# Minimum Window Sort
# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

# Example 1:
# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

# Example 2:
# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

# Example 3:
# Input: [1, 2, 3]
# Output: 0
# Explanation: The array is already sorted

# Example 4:
# Input: [3, 2, 1]
# Output: 3
# Explanation: The whole array needs to be sorted.

def shortest_window_sort(arr):
    # To start, we find the first non sorted element from the right and left
    # Then we find the maximum and minimum of the unsorted window
    # Extend subarray from the beginning to include any number which is bigger than the minimum and therefore unsorted
    # Likewise extend from the end to include any number smaller than the maximum

    left = 0
    right = len(arr) - 1

    while arr[left] <= arr[left + 1]:
        if left + 1 == right: # array is already sorted
            return 0
        
        left += 1

    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1

    window = arr[left : right + 1]
    min = min(window)
    max = max(window)

    while left > 0 and min < arr[left - 1]:
        left -= 1

    while max > arr[right - 1]:
        right += 1

    return right - left + 1

