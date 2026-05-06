"""
We can make two hasmaps and keep a track of frequncy of each letters in the hash maps
THen match the hash maps. If the frequency and letters match then it should work

"""
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)