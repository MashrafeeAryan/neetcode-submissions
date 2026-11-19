class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        U: We are trying to return true if there are same number of characterrs or freqeuncy
        """

        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict