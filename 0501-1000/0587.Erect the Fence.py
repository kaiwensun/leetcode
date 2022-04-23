from collections import defaultdict

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def slope(p1, p2):
            return (p2[1] - p1[1]) / (p2[0] - p1[0])

        coords = defaultdict(list)
        for tree in trees:
            coords[tree[0]].append(tuple(tree))
        for points in coords.values():
            points.sort()
        xcords = sorted(coords.keys())
        # calculate upper border
        upper = []
        for x in xcords:
            point = coords[x][-1]
            while len(upper) >= 2 and slope(upper[-2], upper[-1]) < slope(upper[-1], point):
                upper.pop()
            upper.append(point)
        lower = []
        for x in xcords:
            point = coords[x][0]
            while len(lower) >= 2 and slope(lower[-2], lower[-1]) > slope(lower[-1], point):
                lower.pop()
            lower.append(point)
        left = set(coords[xcords[0]])
        right = set(coords[xcords[-1]])
        return list(map(list, left | right | set(upper) | set(lower)))

