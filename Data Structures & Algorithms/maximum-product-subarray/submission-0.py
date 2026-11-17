class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        We are looking at the largest product subwarray.
        We can loop through nums
        and when we enfounter a negative rpiduct we ask if disregarding thsi product is less that next elemnt we disrad it and start a new subwaa
        """
        high = low = best = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            a = num * high
            b = num * low

            high = max(num,a,b)
            low = min(num,a,b)

            best = max(best, high)
        return best