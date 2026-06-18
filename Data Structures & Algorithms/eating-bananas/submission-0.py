class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        1. The lowest speed is one banana per hour and the highest speed is highest numer of bananas in the array
        2. We use two pointers for this
        3. Let's assume the highest rate of eating banans in least time is equal to the largest pile
        3. while one is less than or equal to the other like binary search condition.
        4. Find the middle speed or k
        5. We use a totalTime variable to track how long it takes
        6. We use a for loop where we go through the array piles
            7. we divide each element by current k and round it to highest closest integer using ceiling function
        8. if totaltime <= h we keep it and store it in res
            9. Then we change the r to mid-1 becuase we want the smallest k that is under that hours
            10. We because we know above mid will finish it within hours
        11. If it is taes more than hours, we move the left pointer and see if a higher k makes sense

        """

        l, r = 1, max(piles)
        res = max(piles)
        while l<=r:
            k = (l+r)//2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k);
            
            if totalTime <= h:
                res = k;
                r = k - 1
            else:
                l = k + 1
        
        return res