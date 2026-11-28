class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #We need the heavisest stone sorted. 
        # We can use a max heap
        # then we can while our heap exists:



        heapq.heapify_max(stones)
        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)

            if x ==  y:
                continue
            
            elif x < y:
                new_y = y - x
                heapq.heappush_max(stones, new_y)

        return stones[0] if stones else 0