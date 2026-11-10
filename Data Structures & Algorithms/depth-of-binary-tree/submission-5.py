# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        U: We need to return the longest path
        M:
        P:
        The easiest way is to use dfs go through the nodes and keep track of the longest path
        """
        
        def dfs(node):
            if node is None:
                return 0
            

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            return 1 + max(left_depth, right_depth)
        
        return dfs(root)