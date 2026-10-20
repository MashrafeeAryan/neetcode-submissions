class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U: We are returning n array of k most frequent elements
        M:
        P:
        Easiest way would be to use dict but then you have to figure out which values are top k
        well can do that by loooping through dict and it still would be O(n)
        """

        nums_dict = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]
        for key, val in nums_dict.items():
            buckets[val].append(key)
        
        result = []

        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

            