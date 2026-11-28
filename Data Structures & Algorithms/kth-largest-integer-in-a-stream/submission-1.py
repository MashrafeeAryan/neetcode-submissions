class KthLargest:
    
    # k
    def __init__(self, k: int, nums: List[int]):
        # they didnt ask for a optimal solution
        # Since duplcaes count we can put it in a min heap
        # and reverse it or thee is max heeap that automatically sorts. 
        # We can use amx heap and po k numer of times
        #Whenw eare adding as well we can still pop k number of ties after adding to maxheap
        self.k = k
        self.heap = []

        for num in nums:
            heapq.heappush(self.heap, num)

            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        
