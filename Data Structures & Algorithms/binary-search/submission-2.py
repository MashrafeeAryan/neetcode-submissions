class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        1. Binary search runs in O(logn)
        2. A left pointer at index - and right pointer at len(nums)-1 index
        3. We have a condition where while l<=r:
        4. we find middle index (l+r)//2
        5. if target greater than middle index:
            6. all numbers less than nums[middleIndex] won't have target
            7. So we move the left pointer to middleIndex+1 
        8. If target less than middle index:
            9. all numbers greater than middle index won't have target
            7. So we move the right pointer to middleIndex -1
        """

        l, r = 0, len(nums)-1

        while l<=r:
            midInd = (l+r)//2
            if nums[midInd] == target:
                return midInd
            elif target < nums[midInd]:
                r = midInd -1
            elif target > nums[midInd]:
                l = midInd +1
        return -1