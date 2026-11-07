class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        U: indices that add up to target
        M:
        P:
        We can create a dict with corresponding index and nums value
        Then we loop through nums:
        we check if target - current value is in seen.
        then we take both indexes and return it
        """
        seen = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in seen:
                return [seen[val], i]
            else:
                seen[nums[i]] = i
        