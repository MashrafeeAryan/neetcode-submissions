class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        U: We just use the same idea of fiding the largest palindrome and instead of finding the largest ones. We just add up the counter every time we find a plaindrome
        """
        count = 0
        for i in range(len(s)):

            #For odd
            l, r = i, i

            while l >= 0 and r<len(s) and s[l] == s[r]:
                count+=1

                l-=1
                r+=1
            #For even
            l, r = i, i+1
            while l >= 0 and r<len(s) and s[l] == s[r]:
                count+=1

                l-=1
                r+=1     
        return count