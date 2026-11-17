class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(house):
            rob1, rob2 = 0, 0

            for money in house:
                temp = max(rob1+money, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        

        if len(nums) == 1:
            return nums[0]
        return max(
            #first
            helper(nums[1:]),

            #last
            helper(nums[:-1])
        )