# Insert Interval

# Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position 
# and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

# Example 1:
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

# Example 2:
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
# Output: [[1,3], [4,12]]
# Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

# Example 3:
# Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
# Output: [[1,4], [5,7]]
# Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].

### I MISREAD THE QUESTION. DID NOT SEE THE NON-OVERLAPPING INTERVALS PART

# To answer question correctly, we can skip all intervals (adding them to output) all intervals whose end < newInterval.start
# Then we just merge intervals until intervals[i].start > end

def insert_interval(intervals, newInterval):
    # intervals already sorted
    # Do same as general but while new interval not yet merged, check its start against next interval to see which should merge first

    start = intervals[0].start
    end = intervals[0].end
    mergedIntervals = []
    isNewIntervalMerged = False

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if not isNewIntervalMerged and newInterval.start <= interval.start:
            if newInterval.start <= end:
                end = max(end, newInterval.end)
                isNewIntervalMerged = True
            else:
                mergedIntervals.append(Interval(start, end))
                start = newInterval.start
                end = newInterval.end
                isNewIntervalMerged = True

        if interval.start <= end:
            end = max(end, interval.end)
        else:
            mergedIntervals.append(Interval(start, end))
            start = interval.start
            end = interval.end


    if not isNewIntervalMerged:
        if newInterval.start <= end:
                end = max(end, newInterval.end)
                isNewIntervalMerged = True
            else:
                mergedIntervals.append(Interval(start, end))
                mergedIntervals.append(newInterval)
                isNewIntervalMerged = True

    return mergedIntervals
        
# Time complexity O(N)
# Space complexity O(N)

        


 