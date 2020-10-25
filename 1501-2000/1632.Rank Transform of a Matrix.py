from collections import defaultdict
class Solution(object):
    def matrixRankTransform(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        smallers = defaultdict(list)
        uf_data = {}
        ans = [[0] * n for _ in xrange(m)]

        def find(x):
            if x not in uf_data:
                uf_data[x] = x
            elif uf_data[x] != x:
                uf_data[x] = find(uf_data[x])
            return uf_data[x]
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                uf_data[rx] = ry

        def find_smallers_and_equals(matrix, is_transpose):
            m, n = len(matrix), len(matrix[0])
            for i in xrange(m):
                num2indexes = defaultdict(list)
                for j, num in enumerate(matrix[i]):
                    num2indexes[num].append((j, i) if is_transpose else (i, j))
                sorted_nums = list(sorted(num2indexes.keys()))
                for k in xrange(len(sorted_nums)):
                    num = sorted_nums[k]
                    if k != 0:
                        smaller = num2indexes[sorted_nums[k - 1]][0]
                        for num_index in num2indexes[num]:
                            smallers[num_index].append(smaller)
                    for t in xrange(len(num2indexes[num]) - 1):
                        union(num2indexes[num][t], num2indexes[num][t + 1])
                        
        def get_rank(point):
            if not ans[point[0]][point[1]]:
                rank = 1
                for equal_point in representative2members[find(point)]:
                    for smaller_point in smallers[equal_point]:
                        rank = max(rank, get_rank(smaller_point) + 1)
                for equal_point in representative2members[find(point)]:
                    assert(ans[equal_point[0]][equal_point[1]] == 0)
                    ans[equal_point[0]][equal_point[1]] = rank
            return ans[point[0]][point[1]]


        find_smallers_and_equals(matrix, False)
        find_smallers_and_equals(zip(*matrix), True)
        
        representative2members = defaultdict(list)  # reverse search of union-find
        for i in xrange(m):
            for j in xrange(n):
                representative2members[find((i, j))].append((i, j))
        for i in xrange(m):
            for j in xrange(n):
                get_rank((i, j))
        return ans

