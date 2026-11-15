class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        U: 

        """

        # THis helps us know which neighbors a node has
        #Ex: index 0 means node 0 has [1] this many neighbors
        graphs = [[] for _ in range(n)]

        #Add the neighbors
        for a,b in edges:
            graphs[a].append(b)
            graphs[b].append(a)

        
        visited = set()
        components = 0

        for node in range(n):
            if node in visited:
                continue
            
            components+=1
            visited.add(node)
            stack = [node]

            while stack:
                current  = stack.pop()

                for neighbor in graphs[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
        
        return components
