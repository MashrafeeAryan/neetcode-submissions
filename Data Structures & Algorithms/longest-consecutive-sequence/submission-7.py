class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We are returning the length of a consecutive sequence
        # We can do that by having a set ( we dont want duplicates)
        # We loop through nums and have a while loop that loops till we find a start of the sequence
        # Whenw e find the start of the sequence we can go ahead and add +1 to and find if th enext numer exists in our set

        # make a set of nums
        nums_set = set(nums)
        longest = 0
        for i in range(len(nums)):

            # We are trtying to get to the start index
            if nums[i]-1 in nums_set:
                continue
            
            # After this we should have a starting point of sequnece
            # nums[i] is start of sequnece
            length = 1 # beccause of num[i]

            while nums[i] + length in nums_set:
                length+=1
                
            longest = max(length, longest)
        
        return longest
