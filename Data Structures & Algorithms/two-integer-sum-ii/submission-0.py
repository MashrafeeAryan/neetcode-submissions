class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Let's try two pointers approach
        1. One pointer starts from index 0
        2. Second pointer starts from index 1
        3. There will be one for loop in range(len(numbers))
        4. There will be another for loop nested in range(len(numbers))

        """

        for i in range(len(numbers)):

            for j in range(1, len(numbers)):
                if numbers[i] + numbers[j] == target and i < j:
                    return [i+1,j+1]