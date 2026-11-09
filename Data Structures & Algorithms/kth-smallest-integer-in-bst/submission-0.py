# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        U: in binary search tree the left is less than root and right is greater than root
        M::
        P: So if we go to all the way left we should findthe smallest value in bianry search tree

        """

        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            

            curr = stack.pop()
            k-=1

            if k==0:
                return curr.val
            
            curr = curr.right
        

