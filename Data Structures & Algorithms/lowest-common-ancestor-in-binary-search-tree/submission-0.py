class Solution:
    def lowestCommonAncestor(self, root: TreeNode,
                             p: TreeNode, q: TreeNode) -> TreeNode:

        # Both targets are smaller: search left
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Both targets are larger: search right
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Their paths split here, or root is one of the targets
        return root