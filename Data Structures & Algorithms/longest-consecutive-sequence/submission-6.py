class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        U: Return the len of longest consecutive sequence.
        M:
        P:
        Since we have to write it in O(n) we cant sort it
        make a set() nums_set of nums
        loop throuhg nums
        set a while loop inside the loop if currentvalue-1 exists in set() then it is not a start of a new series so we move keep doing that till we reach start of the series
        When we reach start of series
        we do another while
        while curr+1 essts in set increase the length by 1

        and take the max 
        """

        longest = 0
        nums_set = set(nums)

        for i in range(len(nums)):

            if nums[i]-1 in nums_set:
                continue
            
            length = 1
            a = nums[i]
            while a +1 in nums_set:
                length +=1
                a+=1

            longest = max(length, longest)
        return longest 