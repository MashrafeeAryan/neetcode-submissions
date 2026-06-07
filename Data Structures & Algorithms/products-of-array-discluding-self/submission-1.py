class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        create an empty array output
        Two loops so O(n^2)
        first loop goes till the range of length of nums
        second loop goes through nums and multiply everything 
        we store in output using index of first loop
        """

        output = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product = product * nums[j]
            
            output.append(product)
        return output

            




        