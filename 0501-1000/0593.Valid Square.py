class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def get_edge_sq2(points):
            p1, p2 = points
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
            
        points = list(sorted([p1, p2, p3, p4]))
        points = [points[i] for i in (0, 1, 3, 2)]
        edges = zip(points, points[1:] + points[:1])
        edge_sq2s = set(map(get_edge_sq2, edges))
        if len(edge_sq2s) != 1 or (edge_sq2:= edge_sq2s.pop()) == 0:
            return False
        if get_edge_sq2((points[0], points[2])) != (diagonal_sq2:=get_edge_sq2((points[1], points[3]))):
            return False
        if diagonal_sq2 != edge_sq2 * 2:
            return False
        return True

