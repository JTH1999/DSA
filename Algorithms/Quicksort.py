def quicksort(arr, lo, hi):
    if lo >= hi:
        return

    # partition array into [< pivot, pivot, > pivot]
    pivotIndex = partition(arr, lo, hi)

    # recursively call quicksort on the < pivot partition
    quicksort(arr, lo, pivotIndex - 1)

    # recursively call quicksort on the > pivot partition
    quicksort(arr, pivotIndex + 1, hi)

    
# set pivot to the last element
# keep pointer of position less than pointer swap position
# step through the array, if element less than pivot element
# increment index and swap arr[i] with arr[index]
# finally increment index again and swap arr[index] with pivot element
def partition(arr, lo, hi):
    pivot = arr[hi]
    index = lo - 1

    for i in range(lo, hi):
        if arr[i] <= arr[pivot]:
            index += 1
            tmp = arr[i]
            arr[i] = arr[index]
            arr[index] = tmp

    # swap pivot with index
    index += 1
    arr[hi] = arr[index]
    arr[index] = pivot

    return index

# Time complextiy - O(nlogn), although in worst case of reverse sorted list it will be n^2

# Space complexity - O(logn) due to call stack memory because of recursive calls
