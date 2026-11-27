class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """"
        U:
        """
        return Counter(s) == Counter(t)