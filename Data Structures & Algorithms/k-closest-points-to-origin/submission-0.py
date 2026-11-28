class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We can just store kth smallest vallues (useful ut might not e necesary)
        # we have to find the euclidean distance oif all the points and then use the distanve as key and coordintes as values. weca ne asilosrt it and get k coset distance

        # what the other idea was to use queue and store kth smallest values only but no poin iin doign hat i dont see any benfit

        heap = []

        for x, y in points:
            distance = x*x + y*y

            heapq.heappush_max(heap, (distance, x, y))

            if len(heap) > k:
                heapq.heappop_max(heap)
        
        return [[x, y] for _, x, y in heap]