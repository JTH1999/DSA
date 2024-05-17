# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

# Example 1:
# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.

# Example 2:
# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.

def merge(intervalsA, intervalsB):
    bIndex = 0
    aIndex = 0
    out = []

    while aIndex < len(intervalsA) and bIndex < len(intervalsB):
        a = intervalsA[aIndex]
        b = intervalsB[bIndex]


        if a.end < b.start:
            aIndex += 1
            continue
        elif b.end < a.start:
            bIndex += 1
            continue

        start = max(a.start, b.start)
        end = min(a.end, b.end)
        out.append(Interval(start, end))

        if a.end <= b.end:
            aIndex += 1
        if b.end <= a.end:
            bIndex += 1
    
    return out

# Time: O(N+M)
# Space: O(1) - ignoring space needed for result list
