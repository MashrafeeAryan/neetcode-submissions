class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        U: We just need to find the largest sum of continous array and return it
        M:
        P:
        largest_sum = 0
        running_sum = 0

        #Loop through nums
        if adding the number makes it negative then just disregard previous numbers and move on

        """
        largest_sum = nums[0]
        running_sum = 0

        for num in nums:
            running_sum += num
            largest_sum = max(running_sum, largest_sum)

            if running_sum <0:
                running_sum =0
            
        return largest_sum