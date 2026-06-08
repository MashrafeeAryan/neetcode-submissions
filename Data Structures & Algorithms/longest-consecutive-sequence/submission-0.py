class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
         1. Convert the nums to a hash map for O(n) lookup
         2. We loop through nums
         3. If num - 1 is not in the hash map, then we check if it is a start of consecutive element sequence
         4. We check if num + 1 in hash_map. If it is not then it is not a start of consecutive element
         5. BUt if it is in hashmap we update our length count and go to the next value using +1
        
        """
        s = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in s:
                next_num = num +1
                length = 1

                while next_num in s:
                    length +=1
                    next_num +=1

                longest = max(longest, length)
        return longest