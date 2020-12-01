class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        if arr:
            diffs = [cmp(a, b) for a, b in zip(arr[:-1], arr[1:])]
            dirc = 0
            res = cnt = 1
            for diff in diffs:
                if diff:
                    if diff == dirc:
                        cnt = 2
                    else:
                        cnt += 1
                        dirc = diff
                else:
                    cnt = 1
                    dirc = 0
                res = max(res, cnt)
        return res

