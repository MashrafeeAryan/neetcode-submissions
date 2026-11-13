class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def reachable(starts):
            seen = set(starts)
            stack = list(seen)

            while stack:
                r, c = stack.pop()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in seen
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))

            return seen

        p_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        a_starts = [(r, cols - 1) for r in range(rows)] + [
            (rows - 1, c) for c in range(cols)
        ]

        pacific = reachable(p_starts)
        atlantic = reachable(a_starts)

        return [[r, c] for r, c in pacific & atlantic]