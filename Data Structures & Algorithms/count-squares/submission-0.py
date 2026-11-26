class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] +=1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for (x,y), freq in self.points.items():
            if abs(px-x) != abs(py-y) or px == x or py  == y:
                continue
            
            res += (
                freq
                * self.points.get((x, py), 0)
                * self.points.get((px, y), 0)
            )

        return res