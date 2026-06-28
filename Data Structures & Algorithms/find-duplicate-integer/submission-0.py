class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        1. Use a hashmap to find duplicates

        """

        seen = set()
        for i in nums:
            if i in seen:
                return i
            else:
                seen.add(i)

    