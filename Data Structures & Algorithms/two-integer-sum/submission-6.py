class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        U: we need to return indices that add up to target
        M:
        P:
        We keep a dict called nums_dict to keep the element of an array as key and index as value
        We loop through nums:
            chheck val = nums[i] - target
            if val in nums_dict:
                return [nums_dict[val], i]

            nums_dict[nums[i]] = i
        """

        nums_dict = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in nums_dict:
                return [nums_dict[val], i]

            nums_dict[nums[i]] = i
        
        