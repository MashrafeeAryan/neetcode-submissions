class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U: We can use a simple bucket sort here
        P: We have as many buckets as len(nums)
        How are we sorting it though
        we use a counter to get frequencies of each nums
        then we can probably use bucket sort 
        and corresponding to the frequencies we add that value in a specific index

        """
        buckets = [[] for _ in range(len(nums)+1)]

        nums_dict = Counter(nums)
        results = []
        for key, freq in nums_dict.items():
            buckets[freq].append(key)
        
        
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                results.append(num)
            
                if len(results) == k:
                    return results