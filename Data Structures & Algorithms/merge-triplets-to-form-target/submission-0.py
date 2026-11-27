class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [0, 0, 0]

        for a, b, c in triplets:

            if a > target[0] or b > target[1] or c > target[2]:
                continue

            result[0] = max(result[0], a)
            result[1] = max(result[1], b)
            result[2] = max(result[2], c)

        return result == target