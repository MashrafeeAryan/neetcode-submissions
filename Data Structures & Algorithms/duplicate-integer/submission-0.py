"""
Can use set() function and it will only return unique values.
If the length of set(nums) = length of nums, then no value appears more than once and
we can return false
Otherwise, we will return true
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_values = set(nums);
        
        if len(unique_values) == len(nums):
            return False;
        else:
            return True;