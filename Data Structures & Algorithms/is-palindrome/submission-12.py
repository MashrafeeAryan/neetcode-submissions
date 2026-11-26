class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we can ise a left vs right pointer and skip the spaces or non alnum() values


        l = 0
        r = len(s)-1

        while l < r:

            while l < r and not s[l].isalnum():
                l+=1
            
            while l < r and not s[r].isalnum():
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1

        return True