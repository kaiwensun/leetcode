class Solution:
    def numOfSubsequences(self, s: str) -> int:
        keyword = "LCT"
        lst = [keyword.index(c) for c in s if c in keyword]
        n = len(keyword)
        left = [[0, 0, 0]]
        for item in lst:
            cur = list(left[-1])
            if item == 0:
                cur[0] += 1
            else:
                cur[item] += cur[item - 1]
            left.append(cur)
        right = [[0, 0, 0]]
        for item in reversed(lst):
            cur = list(right[-1])
            if item == n - 1:
                cur[-1] += 1
            else:
                cur[item] += cur[item + 1]
            right.append(cur)
        right.reverse()
        res = 0
        for l, r in zip(left, right):
            # if not insert anything: r[0] + l[0] * r[1] + l[1] * r[2] + l[2]
            res_l = r[0] + (l[0] + 1) * r[1] + l[1] * r[2] + l[2]
            res_c = r[0] + l[0] * r[1] + (l[1] + l[0]) * r[2] + l[2]
            res_t = r[0] + l[0] * r[1] + l[1] * r[2] + (l[2] + l[1])
            res = max(res, res_l, res_c, res_t)
        return res

