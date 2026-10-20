class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        U: Return the indices of values that add up to target in a list
        M: Hash map
        P: 
        1. we have a hash map
        2. We store the valus with index on hashmap
        3. we do target- current value = x, if x is in hash map we return[current, x]
        4. indices of both
        """

        hash_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_map:
                return [hash_map[diff], i]
            else:
                hash_map[nums[i]] = i

    