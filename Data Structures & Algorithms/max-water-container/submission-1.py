class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we use left and right pointer
        # keep track of max vol
        # vol = right - left + 1 * smallest of both height
        # we move the pointer with smaller height

        left = 0
        right = len(heights)-1
        maxAmount = 0

        while left < right:
            if heights[left] <= heights[right]:
                vol = (right - left) * heights[left]
                maxAmount = max(maxAmount, vol)
                left+=1
            else:
                vol = (right - left) * heights[right]
                maxAmount = max(maxAmount, vol)
                right-=1

        return maxAmount

