class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        U: We are returning the index of which numbers add up to target
        M:
        P:
        Brute force would be ented loops comparing eery single one adding up to target
        Normal; solution would be:
        Plan:
        We have a dict:
        We loop through nums do
        we do 
        target - nums[i] = x

        """
        # if we use a set we can do it
        num_dict = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in num_dict:
                return [num_dict[val], i]

            num_dict[nums[i]] = i
        
        