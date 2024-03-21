# Merge Intervals

# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Example 1:
# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
# one [1,5].

# Example 2:
# Intervals: [[6,7], [2,4], [5,9]]
# Output: [[2,4], [5,9]]
# Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
 
# Example 3:
# Intervals: [[1,4], [2,6], [3,5]]
# Output: [[1,6]]
# Explanation: Since all the given intervals overlap, we merged them into one.

class interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def merge_intervals(intervals):
    # Sort intervals by start
    # We then iterate through intervals, expanding our interval when overlap
    # if interval start > our working interval end, we append interval to mergedintervals array 
    # and interval becomes our new working interval

    if len(intervals) < 2:
        return intervals

    mergedintervals = []
    intervals.sort(key = lambda x: x.start)

    start = interval[0].start
    end = interval[0].end

    for i in range(1, len(intervals)):
        if intervals[i].start <= end:
            end = max(intervals[i].end, end)
        else:
            mergedintervals.append(Interval(start, end))
            start = intervals[i].start
            end = intervals[i].end

    # Need to add final interval
    mergedIntervals.append(Interval(start, end))

    return mergedIntervals

# Time complexity O(NLogN) - only one iteration so O(N) but we sort at the beginning
# which is NLogN complexity

# Space complexity O(N) - need to store up to N intervals in mergedIntervals

        

