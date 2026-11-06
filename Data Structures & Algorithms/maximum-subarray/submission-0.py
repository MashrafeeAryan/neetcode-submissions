class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        u:WE HAVE TO RETURN the largest sub array sum. 
        M: 
        P: We can use a dynamic slding window but when when we encouter negative numbers i is reducing our sums. maybe we judt try to remove it whenever we counter it. not sure

        """

        current_sum = nums[0]
        best_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Should we start a new subarray or continue current one
            current_sum = max(num, current_sum + num)

            best_sum = max(best_sum, current_sum)

        return best_sum