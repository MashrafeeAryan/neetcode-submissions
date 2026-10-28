# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        U: We have to see if it is valid BTS. We just need to make srue left node is smaller than current node and right node is greater than current node
        M: DFs we are looking at the children so we cna do it.
        P:
        1. 
        """

        def dfs(node, lower, upper):
            if node is None:
                return True
            

            # Do
            if not lower < node.val < upper:
                return False
            
            #go dfs()
            left_nodes = dfs(node.left, lower, node.val)
            right_nodes = dfs(node.right, node.val, upper)

            return left_nodes and right_nodes
        
        return dfs(root, float("-inf"), float("inf"))