class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        U: return true if array has duplicates or retunr false
        M: set
        P: We ca just use a sert abnd match the len
        """

        set_nums = set(nums)

        return len(nums) != len(set_nums)