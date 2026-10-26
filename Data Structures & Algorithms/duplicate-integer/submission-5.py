class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        U: If a value in nums appear more than once, we return true
        if a value in nums appear just once, we return false
        M: set()
        P:
        1. define set()
        2. we loop through nums
        3. if not in seen:
            we add it
        5. if in seen:
            return true
        6. if loop ends without true::
        return false
        """

        return len(set(nums)) != len(nums)
        # IF both is the same, all uniqeu values so return false
        #