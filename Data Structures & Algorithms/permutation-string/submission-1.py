class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        We are checking if the three characters are in the window size three in s2. That being said, s2 always has to be greater than s1
        We know the window size will be len(s1)
        """
        from collections import Counter
        if len(s2) < len(s1):
            return False
        s1Dict = Counter(s1)
        l = 0
        for r in range(len(s1)-1, len(s2)):
            s2Dict = Counter(s2[l:r+1])
            if s1Dict == s2Dict:
                return True
            else:
                l+=1
        return False