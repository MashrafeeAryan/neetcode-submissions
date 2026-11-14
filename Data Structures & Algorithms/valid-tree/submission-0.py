class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """ 
        U: Return true if all n nodes are conneted and graph has no cycles
        M:
        P:

        """

        # Create a list that correspons to the number of nodes
        # The index is no_of_node and the array will cintan it's neighbors

        graphs = [[] for _ in range(n)]
        
        for a,b in edges:
            graphs[a].append(b)
            graphs[b].append(a)

        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for neighbor in graphs[node]:

                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return False

                if not dfs(neighbor, node):
                    return False
                
            return True
        
        return dfs(0, -1) and len(visited) == n