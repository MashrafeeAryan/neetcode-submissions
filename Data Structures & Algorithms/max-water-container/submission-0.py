class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r= len(heights)-1
        maxArea = 0
        while l<r:
            minHeight = min(heights[l], heights[r])
            width = r-l
            currArea = width * minHeight
            maxArea = max(maxArea, currArea)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return maxArea