class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        U: Start of sequence is when curr-1 does not exist then we try if curr+1 exists and keep doing that

        """

        #Convert it into a set
        #have a variable for longest
        # We have to find the start of a sequence
        # Loop through nums
        # we check if there is a previous number if not it is a start of squecne
        # we keep trying to look for another one


        longest = 0
        num_set = set(nums)

        for num in nums:
            if num-1 in num_set:
                continue
            length = 1
            while num + length in num_set:
                length+=1
            
            longest= max(length, longest)
        return longest