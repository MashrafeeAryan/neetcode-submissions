# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    """
    U: We have to serialzie it, Maybe something like inorder and preorder list and convert it into a stirng and send it

    """
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens = []
        def dfs(node):
            if node is None:
                tokens.append("#")
                return
            
            tokens.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(tokens)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(","))

        def build():
            token = next(tokens)

            if token == "#":
                return None
        
            node = TreeNode(int(token))

            node.left = build()
            node.right = build()

            return node
        return build()