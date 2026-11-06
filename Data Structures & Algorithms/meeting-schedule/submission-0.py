"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        U: We just need to check if any overlap. If it does return false, otherwise true
        M:
        P:
        if it was a list within a list we would have sorted it but i believe we can still sort it
        1. Sort it using lamda and first element
        2. after sorting check if any overlap.
        3. if not return true
        """
        if not intervals:
            return True

        intervals.sort(key=lambda interval:interval.end) #Can we access a tuple like that
        previous_end = intervals[0].end
        for interval in intervals[1:]:
            # if the start is less than previous end it means it overlaps
            if interval.start < previous_end:
                return False
            
            previous_end = interval.end
        return True
