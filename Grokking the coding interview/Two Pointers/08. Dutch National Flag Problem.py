# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

# Example 1:
# Input: [1, 0, 2, 1, 0]
# Output: [0 0 1 1 2]

# Example 2:
# Input: [2, 2, 0, 1, 2, 0]
# Output: [0 0 1 2 2 2 ]

def dutch_flag_sort(arr):
    # All elements < low are 0, all elements > high are 2
    # All elements from >= low < i are 1
    low = 0
    high = len(arr) - 1
    i = 0

    while i < high:
        if arr[i] < 1:
            temp = arr[i]
            arr[i] = arr[low]
            arr[low] = temp
            low += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        elif arr[i] > 1:
            temp = arr[i]
            arr[i] = arr[high]
            arr[high] = temp
            # Only decrement high - after the swap the number at index i could be 0, 1 or 2
            high -= 1

# Time complexity O(N)
# Space complexity O(1)