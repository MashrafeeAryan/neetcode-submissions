class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        while x!=0:
            digit = x%10 if x>0 else x%-10
            x = (x-digit)//10

            result = result * 10 + digit

            if result > 2**31-1 or result < -2**31-1:
                return 0
        return result