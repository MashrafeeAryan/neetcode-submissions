# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        U: We are flipping left = right and returning the tree
        M:
        P:
        1. Check if root exists if not return None
        2. do a recrusion with def bfs(root)
        3. swith left, right = right, left
        4. after we are done we return root

        """

        def dfs(node):
            if not node:
                return

            node.left, node.right = node.right, node.left

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return root