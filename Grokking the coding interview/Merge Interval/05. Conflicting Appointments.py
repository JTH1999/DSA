# Conflicting Appointments

# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

# Example 1:
# Appointments: [[1,4], [2,5], [7,9]]
# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

# Example 2:
# Appointments: [[6,7], [2,4], [8,12]]
# Output: true
# Explanation: None of the appointments overlap, therefore a person can attend all of them.

# Example 3:
# Appointments: [[4,5], [2,3], [3,6]]
# Output: false
# Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.

def can_attend_all_appointments(intervals):
    intervals.sort(key = lambda x: x.start)
    index = 0

    while index < len(intervals) - 1:
        if intervals[index].end > intervals[index + 1].start:
            # Note that it is > not >= since if start == end then there is no conflict
            return False
        
        index += 1

    return True

# Time: O(NLogN) for the sort
# Space: O(N), also for the sort