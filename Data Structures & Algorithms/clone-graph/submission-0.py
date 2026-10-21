"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        U: We are trying to replicate the graph
        M:
        P:
        """

        if not node:
            return None

        clones  = {}
        def dfs(original):
            if original in clones:
                return clones[original]

            
            copy = Node(original.val)
            clones[original] = copy

            for neighbor in original.neighbors:
                copied_neighbor = dfs(neighbor)
                copy.neighbors.append(copied_neighbor)

            return copy
        
        return dfs(node)
            