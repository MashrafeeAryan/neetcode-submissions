class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        1. We start witha number the first element to get something
        2. We initialzie the pointers ith l = 0 and r = len(nums)-1
        3. while l<=r
        4.We check if the first element of the window is less than the last element of the window, then we got our perfect array
        5. Our first element of the rotated array is minimum
        6. Then we check between minimum we have to minimum of middle element
        7. We then find the middle index.
        8. If the middle element is greater than the left pointer element than the first array is sorted
        9. we move te pointer l = m +1
        10. if middle element << left pointer element h+tuenn ithe left side has minimum

        """

        l, r = 0, len(nums)-1;
        res = nums[0]

        while l<=r:
            if nums[l] < nums[r]:
                res =  min(res, nums[l])
                break
            
            mid = (l+r)//2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid +1
            else:
                r = mid - 1
        return res
        