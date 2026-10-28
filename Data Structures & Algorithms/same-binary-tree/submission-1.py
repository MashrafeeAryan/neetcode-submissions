# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        U: We have to check if both binary tree same structure nodes have same values
        M: bfs
        """

        def dfs(node1, node2):
            #Stop
            if node1 is None and node2 is None:
                return True

            if node1 is None and node2 is not None:
                return False
            
            if node1 is not None and node2 is None:
                return False
            
            #Do
            if node1.val != node2.val:
                return False
            

            #Go
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right
        
        return dfs(p, q)