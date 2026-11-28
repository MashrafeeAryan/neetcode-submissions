class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # I mean heap min aslso does some sort of sorting 
        # The complextiy would be O(logn)

        # I will use a min heap and then pop oout to keep the kth largest elemtns

        heap = []
        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]