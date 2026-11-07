class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        U:  We have to find the longest consecutive seqeunce and return the len
        M:
        P:
        1. 

        """

        longest = 0
        length = 0

        nums_set = set(nums)

        for num in nums:
            if num - 1 in nums_set:
                continue
            
            length = 1
            while num + length in nums_set:
                length +=1
            
            longest = max(length, longest)
        
        return longest