class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1. We can go through each element in row and columns and check target, which would be brute force.
        2. We can go through each row and check the last element. If the last element is greater than target, then the target is in that row
        3. We can do a binary search in that row and get our target.
        """

        for r in range(len(matrix)):
            if matrix[r][-1] == target:
                return True
            elif matrix[r][-1] > target:
                l = 0
                lastPointer = len(matrix[r])-1
                while l<=lastPointer:
                    midPointIndex = (l+lastPointer)//2
                    if matrix[r][midPointIndex] == target:
                        return True
                    elif matrix[r][midPointIndex] < target:
                        l = midPointIndex +1

                    elif matrix[r][midPointIndex] > target:
                        lastPointer = midPointIndex -1  

                return False
        return False