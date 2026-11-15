
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        start, end = newInterval[0], newInterval[1]

        # Step 1: Add intervals that come before newInterval
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # Step 2: Merge overlapping intervals
        while i < n and intervals[i][0] <= end:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1

        # Step 3: Insert the merged interval
        result.append([start, end])

        # Step 4: Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
