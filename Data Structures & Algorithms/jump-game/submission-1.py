class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Our goal is to reach the end len(nums)-1. We can take the maximum no. of steps that is inside a nums[i]. We can go less or go more.
        M:
        P:
        """

        farthest = 0

        last = len(nums)-1

        for i, jump in enumerate(nums):

            # I > farthest
            # if it is greater, it means the farthest can't reach i.
            # So all the jumps we did cannot reach i
            if i > farthest:
                return False

            # The idea is simple
            # We just want to see what is the furthest we can jump from a given index
            farthest = max(farthest, i + jump)

            if farthest >= last:
                return True
        
        # The for loop helps us verify all the jumps till farthest.
        # So 
        return False