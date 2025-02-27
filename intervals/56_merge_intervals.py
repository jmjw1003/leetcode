from collections import deque

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        intervals = deque(intervals)
        merged_intervals = []
        current_interval = intervals.popleft()
        while intervals:
            new_interval = intervals.popleft()
            if new_interval[0] <= current_interval[1]:
                current_interval[1] = max(current_interval[1], new_interval[1])
            else:
                merged_intervals.append(current_interval)
                current_interval = new_interval
        merged_intervals.append(current_interval)
        return merged_intervals
