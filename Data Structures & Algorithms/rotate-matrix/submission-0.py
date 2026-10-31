class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        U: We need to change the matrix in place adn return after doing 90- degree rotation 
        M: 
        P:
        Seems like i can tranpose it first row is last column, scond row is second column, last row is first column
        """
        n = len(matrix)
        for row in range(n):
            for col in range(row+1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            
        for row in matrix:
            row.reverse()