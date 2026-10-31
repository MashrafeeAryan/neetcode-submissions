class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        U: return a list of array that contains the number of 1s in binary for that particular index
        M:
        P:
        1. have a results
        2. have a count array
        3. the same idea to find 1s in n:
    

        """

        result = []

        for curr in range(0, n+1):
            count = 0
            while curr:
                curr = curr & curr - 1
                count +=1
            result.append(count)
        return result
        