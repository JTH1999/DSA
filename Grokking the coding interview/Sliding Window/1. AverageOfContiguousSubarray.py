# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# https://glucko.github.io/codeprep/GrokkCode/2._Pattern_Sliding_Window/1._Introduction/1.2_Introduction_-_Grokking_the_Coding_Interview__Patterns_for_Coding_Questions.html#

def average_of_subarrays(k, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element to the sum

        # slide the array - not needed until at kth element
        if windowEnd >= k - 1:
            result.append(windowSum / k) # calculate the average
            windowSum -= arr[windowStart] # remove the first from the window
            windowStart += 1 # slide the window ahead

    return result
        