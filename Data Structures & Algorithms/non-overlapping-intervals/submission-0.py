class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        U: find how many intervals overlap and if we remove the minimum number of them can we prevent the overlap
        M;
        P: if we sort them
        then we keep track of how many times it overlaps
        so we go through start,end and whenver we encoutner a oerlap we skip it increase our count and see if it still overlaps with the next interval

        """

        removed = 0
        intervals.sort(key= lambda interval:interval[1])
        previous_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < previous_end:
                removed+=1
            else:
                previous_end = end
        
        return removed