class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        U: We have two pointers left and right and keep mathcing them to see if it is eactly the same
        M:
        P: 
        1. We have two pointers both left and right
        2. we skip it if it's not alpha num
        3. when we encounter an alpha num we match them but migt need to lower
        """

        left = 0
        right  = len(s)-1

        while left <= right:

            while left < right and not s[left].isalnum():
                left +=1
            
            while left< right and not s[right].isalnum():
                right -=1
            
            # .lower() won't work on digits
            if s[left].lower() != s[right].lower():
                return False
            
            left+=1
            right-=1
        return True
