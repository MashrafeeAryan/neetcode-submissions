class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        U: return an array with product except self
        M:
        P:
        we first get the product of every element and it's left side
        we then get the prouct of eveyr element and it's right side
        """

        result = [1]*len(nums)
        left = 1
        for i in range(len(nums)):
            result[i] = left
            left *= nums[i]

        
        right = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result