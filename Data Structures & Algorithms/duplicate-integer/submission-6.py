class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        U: Return true if there is a duplicate, otherwise return False
        M:
        P:  Compare len(nums) != len(set(nums))
        if it is equal length then it is not a duplciate thus it will give false, it is not of equal length there was a dupicate and give true                                                                                            
        """

        return len(nums) != len(set(nums))