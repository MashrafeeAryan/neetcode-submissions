from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        We use from collectiosn import Counter to get frequencies of each element.
        The keys are elements and values are frequencies
        If the input array is in order, we can use the values to access hash and get the keys. 
        Use frequency coutners to count how many times each nummbers appear
        Populate the bbuckets where index represents the frequency.
        """

        freq = Counter(nums);

        bucket = []
        for _ in range(len(nums)+1):
            bucket.append([])

        for key, value in freq.items():
            bucket[value].append(key)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res;