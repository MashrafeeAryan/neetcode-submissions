class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        U: We are searching for the word using backtracking
        M:
        P: have a path = []
        1. our base case is if path.join matches target
        or we can use remainign array and check
        then we loop through from start to end each row and col
        """

        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):

            if i == len(word):
                return True
            if (r < 0 or r >= rows) or (c< 0 or c>=cols) or (board[r][c] !=word[i]):
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            found = (
            dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1)
            )


            board[r][c] = temp
            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, 0):
                    return True
        
        return False
