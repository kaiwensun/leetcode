class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """

        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]

        def union(x, y):
            global res
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                data[rootx] = rooty
                size[rooty] += size[rootx]

        if m == len(arr):
            return m
        data = range(len(arr))
        size = [0] * len(arr)
        res = -1
        for step, index in enumerate(arr):
            i = index - 1
            size[i] = 1
            if i != 0 and size[find(i - 1)] == m:
                res = step
            if i != len(arr) - 1 and size[find(i + 1)] == m:
                res = step
            if i != 0 and size[i - 1] != 0:
                union(i, i - 1)
            if i != len(arr) - 1 and size[i + 1] != 0:
                union(i, i + 1)
        return res

