# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        U: We are checking if a subroot has same chidren and aprt of root. If no subroot, then it is part of root
        M: dfs
        P: We implmenet same tree search to find subroot. We have to go through root and find the starting root of of subrrot in the main tree and then try sametree funcion
        """

        def sameTree(node1, node2):
            if node1 is None and node2 is None:
                return True
            
            if node1 is None or node2 is None:
                return False
            
            if node1.val != node2.val:
                return False

            left_same = sameTree(node1.left, node2.left)
            right_same = sameTree(node1.right, node2.right)

            return left_same and right_same
        
        
        def search(node):
            if node is None:
                return False

            if sameTree(node, subRoot):
                return True
            
            return search(node.left) or search(node.right)

        if subRoot is None:
            return True
        
        return search(root)

