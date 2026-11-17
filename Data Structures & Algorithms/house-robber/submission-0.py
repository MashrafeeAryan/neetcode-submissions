class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        U: We need the get the maximum amount of money while avoiding robbing adjacent houses.
        M:
        P: IF we had a dict with index and corresping house money value we can probalby do something.

        """
        rob1, rob2 = 0, 0

        for money in nums:
            temp = max(money + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2