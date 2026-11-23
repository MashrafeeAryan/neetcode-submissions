class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U: return the most frequnt integers
        M:
        P:
        We use bucket sort
        Each bucket index will tell how many frequncies the values in the buckers have
        we create a bucket 
        buckets = [[] for _ in range(len(nums)+1)]

        now we loop through nums
        or we can create a counter(nums)
        it will create a dict with freq of each element
        we loop throuhg the keys and frequncies
        and put the numbers in buckets
        then we loop throuigh end of bucket till we find k values
        """

        result = []
        buckets = [[] for _ in range(len(nums)+1)]

        nums_dict = Counter(nums)

        for val, freq in nums_dict.items():
            buckets[freq].append(val)
            
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result
        return []