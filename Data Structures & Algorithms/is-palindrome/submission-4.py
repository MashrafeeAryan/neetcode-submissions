class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        U: return true if a string is same from front or reverse
        M:
        P:
        brute force it:
        strip of paces or non alpha nums push it to list.
        reverse it and match orginal vs new

        Optimal solution:
        two pointers
        one on left and one on right
        1. Both left and right pointer should point to same value
        2. However, the alues must be .isalnum() #apha num
        3. we do a while loop while left < right
        4. we have anoter while loop that moves left till it deosnt encoutner alpahnum
        5. we have another while loop that moves right till it encoutners alphanum
        6. when t encoutners we check if they are equal
        """

        left = 0
        right = len(s)-1

        while left < right:

            while left < right and not s[left].isalnum():
                left+=1

            while left < right and not s[right].isalnum():
                right-=1
            
            if s[left].lower() == s[right].lower():
                left+=1
                right-=1
            else:
                return False
        return True