class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        # We add it to the lower first
        heapq.heappush_max(self.lower, num)

        # We move it to the upper 
        largest_lower = heapq.heappop_max(self.lower)
        heapq.heappush(self.upper, largest_lower)
        if (len(self.upper) > len(self.lower)):
            #We move it back
            smallest_upper = heapq.heappop(self.upper)
            heapq.heappush_max(self.lower,smallest_upper)
        

    def findMedian(self) -> float:

        if len(self.lower) > len(self.upper):
            return self.lower[0]
        
        return (self.lower[0] + self.upper[0])/2
        
        