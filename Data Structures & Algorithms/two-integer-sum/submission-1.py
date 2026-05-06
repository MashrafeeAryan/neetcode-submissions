"""
I want to use two-pointer solution
[3,4,5,6]
one pointer (i) will be at 0 index 
another pointer (j) will be at 1 index
We keep i at it's position, and move j
we move j till the end of the list and if i+j does not addd up to target,
we move i one position and then keep repeating it

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed], i]
            seen[nums[i]] = i
        