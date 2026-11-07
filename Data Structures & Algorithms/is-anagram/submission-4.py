class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        y: fREQEUNCY OF CHARACTERS ARE EXACTLY THE SAME
        m:
        p:
        wE USE coUNTER AND MATCH THEM
        """

        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict