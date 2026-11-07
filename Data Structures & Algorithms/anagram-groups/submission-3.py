class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        U: we need group same frequency wordsd in a list and return it
        M:
        P:

        We create an array of 26 0s. we go through each word and populate the array and add it to the key. the idea is we use corresponding index to populate the array
        We convert that array ito tuple to use as a a key and add the word in a list of that key

        """

        word_dict = {}

        for word in strs:
            arr = [0] * 26
            for char in word:
                index = ord(char) - ord("a")

                arr[index]+=1
            
            key = tuple(arr)
            if key not in word_dict:
                word_dict[key] = []
            
            word_dict[key].append(word)
        
        return list(word_dict.values())