class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        U: return indices of numbers that add up to target
        M: Hashmap
        P:
        We will keep a hashmap of values we have seen
        1. loop through nums
        2. if target-current in hash_map:
            return [hash_map[target-current], current]
        """

        hash_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hash_map:
                return [hash_map[diff], i]
            
            hash_map[nums[i]] = i
        
        #We will get a pair we are guranted