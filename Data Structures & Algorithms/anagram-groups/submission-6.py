class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        string_dict = defaultdict()
        for string in strs:
            characters = [0] *  26
            for char in string:
                key = ord(char) - ord("a")
                characters[key]+=1
            
            dict_key = tuple(characters)
            if dict_key in string_dict:
                string_dict[dict_key].append(string)
            else:
                string_dict[dict_key] = [string]
        

        return [i for i in string_dict.values()]