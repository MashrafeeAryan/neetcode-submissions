class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        We have two pointers at index 0 and last index
        1. We add the the pointers and divide by 2 and round it to nearest integer to find the midpoint index.
        2. If the midpoint is less than target, we move the left pointer to midpointIndex + 1 and repeat step1
        3. If the midpoint is greater than target, we move the right pointer to midPointIndex -1 and repet step1
        4. What happens if len(nums) = 0 or len(nums) =1 
    
        """
        
        l, r = 0, len(nums)-1

        while l<=r:
            midPointIndex = int((l+r)/2)
            if nums[midPointIndex] == target:
                return midPointIndex;
            elif nums[midPointIndex] > target:
                r = midPointIndex - 1
            elif nums[midPointIndex] < target:
                l = midPointIndex +1
        return -1 
