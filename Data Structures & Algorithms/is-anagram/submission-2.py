class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        U: Return true if both s and t has ketters that apears same number of times in both strings.
        M: dict
        P:
        1. have two dicts
        2. just compare them
        3. if same, true or else false
        """

        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict
