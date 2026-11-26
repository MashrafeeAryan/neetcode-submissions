class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # this is sorted
        # we can use two pointers
        # not binary search
        # we can set up let and right pointer
        # if sum of left and right > target, reduce right, else increase elft

        left = 0
        right = len(numbers) -1
        while left < right:
            total = numbers[left]+ numbers[right]

            if total < target:
                left+=1
            elif total > target:
                right-=1
            else:
                return [left+1, right+1]
        