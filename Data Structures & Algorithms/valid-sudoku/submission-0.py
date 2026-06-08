class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1. Go through each row and column and see if there are duplicates using for loops and sets
        """

        #checks for duplicates in rows
        for rows in range(9):
            s = set()
            for cols in range(9):
                if board[rows][cols] in s:
                    return False
                elif board[rows][cols] != ".":
                    s.add(board[rows][cols])
        # Checks for duplicates in columsn
        for rows in range(9):
            s = set()
            for cols in range(9):
                if board[cols][rows] in s:
                    return False
                elif board[cols][rows] != ".":
                    s.add(board[cols][rows])

        #Check for duplicates in small boxes
        # we need starting value for each boxes
        start = [(0,0), (0, 3), (0, 6), 
                (3,0), (3, 3), (3, 6),
                (6,0), (6,3), (6,6)
        ]

        for i, j in start:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if board[row][col] in s:
                        return False
                    elif board[row][col] != ".":
                        s.add(board[row][col])
        return True