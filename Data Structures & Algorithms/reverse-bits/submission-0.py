class Solution:
    def reverseBits(self, n: int) -> int:
        """
        U: Reverse n asa string convert it into digits and covnert bin to decimal and return
        P: we start reading from the end of n. or we can just shift it to left by some number. if we start reading from end  we cna do somethi
        """


        result = 0

        for _ in range(32):
            bit = n & 1 # get the last bit
            result = (result<<1) | bit
            n >>= 1
        
        return result
