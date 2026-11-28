class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        results = [1]*len(nums)

        left = 1
        for i in range(len(nums)):
            results[i] *= left
            left *= nums[i]

        right = 1
        for j in range(len(nums)-1, -1, -1):
            results[j] *= right
            right *= nums[j]
        
        return results