class Solution:
    def climbStairs(self, n: int) -> int:
        """
        U: How many combinations of 1s or 2s can we use to get to n
        M:
        P:
        can we use dfs back track?
        we try a step and then tyr another
        """

        one, two = 1, 1

        for _ in range(n-1):
            one, two = one+two, one

        return one