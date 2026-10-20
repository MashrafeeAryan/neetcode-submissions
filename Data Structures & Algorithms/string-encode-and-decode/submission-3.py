class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += (str(len(word)) + '#' + word)
        
        return result
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i

            while s[j]!=  "#":
                j+=1


            length = int(s[i:j])

            #so i at length and j at #
            result.append(s[j+1:j+length+1])

            i = j +length + 1
        
        return result
            
