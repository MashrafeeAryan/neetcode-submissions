# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        U: We ajve to return the depth of tree
        M: Can do with bfs or dfs
        P:
        1. we have a fucntion that has node as a paprementer
        2. if node is noe we return 0
        3. we try to find th left depth and right
        4. left_depth = dfs(node.left)
        5. right_depth = dfs(node.right)
        6. return 1 + max(left_depth, right_depth)

        """


        def dfs(node):
            if node is None:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            return 1 + max(left_depth, right_depth)

        return dfs(root)