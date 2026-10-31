class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        U: Return the number of 1s in binary form of n
        M:
        P: Maybe convert it into binary and then count the 1s

        """
        count = 0
        while n:
            n = n & (n-1) 
            count +=1
        
        return count