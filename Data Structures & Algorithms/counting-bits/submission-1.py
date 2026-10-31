class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for curr in range(1, n + 1):
            result[curr] = result[curr & (curr - 1)] + 1

        return result