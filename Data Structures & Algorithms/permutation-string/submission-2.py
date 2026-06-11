from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        s1Dict = Counter(s1)
        # 1. Initialize s2Dict with just the first window's characters (minus the last one)
        # This keeps our upcoming loop perfectly aligned with your original logic.
        s2Dict = Counter(s2[:len(s1)-1])
        
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            # 2. Add the NEW character entering the window from the right
            s2Dict[s2[r]] = s2Dict.get(s2[r], 0) + 1
            
            # 3. Check if the windows match
            if s1Dict == s2Dict:
                return True
                
            # 4. Slide the window: Prepare for the next iteration by removing the leftmost character
            s2Dict[s2[l]] -= 1
            if s2Dict[s2[l]] == 0:
                del s2Dict[s2[l]] # Clean up empty keys so hash maps match perfectly
                
            l += 1
            
        return False