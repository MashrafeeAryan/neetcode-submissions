class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        We just have to make a conter dict and comapre them
        """
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict