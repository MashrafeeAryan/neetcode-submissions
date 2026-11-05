class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        U: All of the intervals are alredy in ascending order. New interval can be overlapping. We check between which intervals the new interval should go. If it overlaps with other intervals, we combine them
        M:
        P:
        We can go through th eoutput check where the newInterval first element goes.
        So our current interval end range compare it with newInternval start range.. 
        It helps us figure out if it is within a range of intervals we already have. 


        """

        result = []

        for i, (start, end) in enumerate(intervals):

            #We are checking if the current interval start is less than the start of newinterval
            #it means current intveral doesnt voerlap and should be before new interval
            if end < newInterval[0]:
                result.append([start, end])
            
            # If the end < start of new interval
            elif start > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result

            else:
                newInterval = [
                    min(start, newInterval[0]),
                    max(end, newInterval[1])
                ]
            
        result.append(newInterval)
        return result