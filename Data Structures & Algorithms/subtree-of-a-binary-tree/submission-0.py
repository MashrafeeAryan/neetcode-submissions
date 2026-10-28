# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        U: We are checkign if subroot is part of the root wiht same exact structure
        M: Dfs because we have to check on the children. answer depnds on children
        P:
        Maybe using dfs we search for the root of subroot.
        2. we then see if the strcutre amtches but it will fail if there are more than oen same values of the root of subroot

        """

        def sameTree(node1, node2):
            if node1 is None and node2 is None:
                return True
            
            if node1 is not None and node2 is None:
                return False

            
            if node1 is None and node2 is not None:
                return False
            
            if node1.val != node2.val:
                return False
            

            left_depth = sameTree(node1.left, node2.left)
            right_depth = sameTree(node1.right, node2.right)

            return left_depth and right_depth
        

        if root is None:
            return False

        if subRoot is None:
            return True

        if sameTree(root, subRoot):
            return True
        

        return (self.isSubtree(root.left, subRoot)
        or self.isSubtree(root.right, subRoot))