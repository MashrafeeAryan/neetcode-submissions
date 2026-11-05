class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build the trie just like in addWord.
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        found = []

        def dfs(row, col, node):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            char = board[row][col]
            if char == "#" or char not in node.children:
                return

            # The current board cell matches the next trie letter.
            node = node.children[char]

            if node.word is not None:
                found.append(node.word)
                node.word = None  # Report each word only once.

            board[row][col] = "#"  # This path has used this cell.

            dfs(row - 1, col, node)  # Up
            dfs(row + 1, col, node)  # Down
            dfs(row, col - 1, node)  # Left
            dfs(row, col + 1, node)  # Right

            board[row][col] = char  # Let other paths use this cell.

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return found