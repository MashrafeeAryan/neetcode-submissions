class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U: We need return k most frequet elements of the array
        M:
        P: brute froce use a counter have frequnecies.
        Go through the dict and find k time s highest frequencis
        We needa counter but with some other data strucutre where we can organize the numbers with highest freuqncies

        """

        # We use bucket sort. BUcket sort youhave freq in the same index as much as the freq

        buckets = [[] for _ in range(len(nums)+1)]

        nums_freq = Counter(nums)

        for num, freq  in nums_freq.items():
            buckets[freq].append(num)
        
        result = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

