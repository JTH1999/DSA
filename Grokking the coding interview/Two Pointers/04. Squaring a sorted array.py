# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

# Example 1:
# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

# Example 2:
# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9]

def make_squares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    insertionIndex = n - 1
    right = n - 1
    left = 0
    
    while left < right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        
        if leftSquare > rightSquare:
            squares[insertionIndex] = leftSquare
            left += 1
        else:
            squares[insertionIndex] = rightSquare
            right -= 1
        
        insertionIndex -= 1
        
    return squares
            
# Time complexity O(N) - one traversal of the array
# Space Complexity O(N) - space used for output array