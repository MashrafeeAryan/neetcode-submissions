# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Brute force method would be to go through all routes.
        We have a counter we keep going through a single routem then we

        """

        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) +1