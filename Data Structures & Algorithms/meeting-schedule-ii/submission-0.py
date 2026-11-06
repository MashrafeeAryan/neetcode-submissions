"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
    	U: We have to find the minimum rooms to schedule a meeting
        M:
        P:
        We can use the same room if they don't overlap. We have to use a seperate room only if they overlap
        1. We can just sort all of the intervals using the start index
        2. keep a variable for no. of rooms
        3. check if it overlaps. if it does we can say need a room for this one
        4. this woht work
        """
        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)
        max_rooms = 0
        rooms =0
        start_pointer = 0
        end_pointer = 0

        while start_pointer < len(intervals):
            #Check if meeting is starting
            if starts[start_pointer] < ends[end_pointer]:
                rooms+=1
                start_pointer+=1
                max_rooms = max(rooms, max_rooms)
            else:
                rooms-=1
                end_pointer+=1
        
        return max_rooms
