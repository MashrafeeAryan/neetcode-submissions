from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            letters = [0] * 26

            for char in word:
                letters[ord(char) - ord("a")] += 1

            key = tuple(letters)
            groups[key].append(word)

        return list(groups.values())