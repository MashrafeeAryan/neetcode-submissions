class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if we use a set then it wont be O(1)
        result = 0
        for num in nums:
            result ^= num
        
        return result