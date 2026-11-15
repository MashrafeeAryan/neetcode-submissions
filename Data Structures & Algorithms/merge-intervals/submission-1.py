class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        U: We just have to merge tje intervals. first sort them out wit the start
        IF two intervals overlap:
            end of first interval > start of second interval
            we can then combine them

        """

        intervals.sort(key=lambda x:x[0])

        result = [intervals[0]]

        for start, end in intervals[1:]:

            #it overlaps
            if result[-1][1] >= start:
                result[-1][1] = max(end, result[-1][1])
            else:
                result.append([start, end])
        return result