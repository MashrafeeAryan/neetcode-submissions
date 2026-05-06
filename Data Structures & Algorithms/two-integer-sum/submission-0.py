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
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]