class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # We can just loop through all the rows and cols if we encounter 0 we say stop
        # we can creater a helper function to convert whole row and column into 0s
        # we can do loop through the row and 0 and loop throught he column and 0
        rows, cols = len(matrix), len(matrix[0])

        firstRow = any(matrix[0][c] == 0 for c in range(cols))
        firstCol = any(matrix[r][0] == 0 for r in range(rows))
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
    
        if firstRow:
            for c in range(cols):
                matrix[0][c] = 0
            
        if firstCol:
            for r in range(rows):
                matrix[r][0] = 0