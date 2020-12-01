class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        equals = [(eq[0], eq[-1]) for eq in equations if eq[1] == "="]
        inequals = [(eq[0], eq[-1]) for eq in equations if eq[1] == "!"]
        data = {num : num for num in set(eq[0] for eq in equations) | set(eq[-1] for eq in equations)}

        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                data[rx] = ry

        for a, b in equals:
            union(a, b)
        for a, b in inequals:
            if find(a) == find(b):
                return False
        return True

