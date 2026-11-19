class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        U: this is a bucket sort problem

        """

        # so we have 26 alphabets
        # We will use each corresponding index to the alphabet in an array
        # convert it into a tuple
        # use as a key in freq and add the elemts
        strs_dict = {}

        for i in strs:
            alpha_key = [0]*26
            for char in i:
                key = ord(char) - ord("a")
                alpha_key[key] +=1
            
            dict_key = tuple(alpha_key)
            if not dict_key in strs_dict:
                strs_dict[dict_key] = [i]
            else: 
                strs_dict[dict_key].append(i)

        return [i for i in strs_dict.values() ]