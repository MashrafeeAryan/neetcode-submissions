class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        U: return true if exact leeters from start and back
        M:
        P:
        1. we have a left and rigth pointer
        2. we move the left pointer until we reach a isalpha() character it avoids letters that are not alphanurec and numbers
        3. we move the
        """

        left = 0
        right = len(s)-1

        while left<=right:

            while left < right and not s[left].isalnum():
                left+=1
            
            while left < right and not s[right].isalnum():
                right-=1
            
            if s[left].lower() != s[right].lower():
                return False

            left+=1
            right-=1
        return True