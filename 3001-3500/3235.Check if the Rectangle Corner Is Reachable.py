class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:

        def find(x):
            if data[x][0] != x:
                data[x] = find(data[x][0])
            return data[x]
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx[0] != ry[0]:
                ry[1] = ry[1] or rx[1]
                ry[2] = ry[2] or rx[2]
                data[rx[0]] = ry
            # does ry group touching both sides
            return ry[1] and ry[2]
        def is_contact(i, j):
            x1, y1, r1 = circles[i]
            x2, y2, r2 = circles[j]
            return (r1 + r2) ** 2 >= (x1 - x2) ** 2 + (y1 - y2) ** 2

        def is_unionable(i, j):
            # if the overlay area is fully or partially out side of the rectangle,
            # then it doesn't affect the union result
            x1, y1, r1 = circles[i]
            x2, y2, r2 = circles[j]
            return 0 <= x1 * (r1 + r2) + (x2 - x1) * r1 <= X * (r1 + r2) and \
                0 <= y1 * (r1 + r2) + (y2 - y1) * r1 <= Y * (r1 + r2)

        def is_segment_touching_circle(circle, point1, point2):
            if point1[0] == point2[0]:
                # vertical segment, transform to horizontal segment
                circle = (circle[1], circle[0], circle[2])
                point1 = tuple(reversed(point1))
                point2 = tuple(reversed(point2))
                return is_segment_touching_circle(circle, point1, point2)
            # horizontal segment
            # if any point is in or on circle, it is touching
            for p in point1, point2:
                if (circle[0] - p[0]) ** 2 + (circle[1] - p[1]) ** 2 <= circle[2] ** 2:
                    return True
            # if two points are on the same side of the circle (left/right), then not touching
            if point1[0] < circle[0] != point2[0] < circle[0]:
                return False
            y = point1[1]
            return abs(y - circle[1]) <= circle[2]
        def is_circle_touching_topleft(i):
            return is_segment_touching_circle(circles[i], (0, 0), (0, Y)) or is_segment_touching_circle(circles[i], (0, Y), (X, Y))
        def is_circle_touching_bottomright(i):
            return is_segment_touching_circle(circles[i], (0, 0), (X, 0)) or is_segment_touching_circle(circles[i], (X, 0), (X, Y))

        n = len(circles)
        data = [[i, is_circle_touching_topleft(i), is_circle_touching_bottomright(i)] for i in range(n)]
        for i in range(n):
            if data[i][1] and data[i][2]:
                return False
            for j in range(i + 1, n):
                if is_contact(i, j) and is_unionable(i, j):
                    if union(i, j):
                        return False
        return True

