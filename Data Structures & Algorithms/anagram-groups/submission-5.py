class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        U: We are making sublsits of anagrams and returning it
        M:
        P:
        anagram_dict
        we loop through strs
        we loop through each character of strs
        we do:
            index = ord("a") - ord(char)
            character[index] +=1
        key = tuple(character)
        if key in anagram_dict:
            anagram_dict[key].append(str)
        else:
            anagram_dict[key] = [str]

        """
        anagram_dict = {}

        for st in strs:
            character = [0]*26
            for char in st:
                index = ord("a") - ord(char)
                character[index] +=1
            
            key = tuple(character)

            if key in anagram_dict:
                anagram_dict[key].append(st)
            else:
                anagram_dict[key] = [st]
            
        
        return [i for i in anagram_dict.values()]