class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        U: Get the su with add and -
        M:
        P:
        We cna use binary numbers
        witoout carry we know if it matches it has to be 0 so XOR
        but we hwo we track of carry
        """


        mask = 0xFFFFFFFF
        
        # limits a and b to 32 bits
        a = a & mask
        b = b & mask

        while b:
            # Find the binary carry in an addition and mvoe to the left
            carry = ((a & b) << 1) & mask # keep under 32 bits
            a = (a ^ b) & mask # Sum without carry
            b = carry

        if a <= 0x7FFFFFFF:
            return a
        
        return ~(a ^ mask)
