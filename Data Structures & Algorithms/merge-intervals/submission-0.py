class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        U: We have to find overlapping intervals and merge them and return them
        M: 
        P; We sort them first by the first start element
        if end of current interval less than end of next interval it merges
        we create a ewinterval using min of start of both intervals and amx of both end internvals

        """
        intervals.sort(key=lambda interval:interval[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            previous_end = result[-1][1]
            if start <= previous_end:
                result[-1][1] = max(end, previous_end)
            
            else:
                result.append([start,end])
        
        return result
        