class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]* len(nums)

        # DO left side first
        left = 1
        for i in range(len(nums)):
            result[i] *= left
            left*= nums[i]

        #do right
        right = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result
            