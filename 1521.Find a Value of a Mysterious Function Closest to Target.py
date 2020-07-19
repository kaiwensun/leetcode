class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr2 = [arr[0]]
        for a in arr:
            if a != arr2[-1]:
                arr2.append(a)
        arr = arr2
        res = 0xffffffff
        for l in xrange(len(arr)):
            ans = 0xffffffff
            for r in xrange(l, len(arr)):
                ans &= arr[r]
                if target - ans >= res:
                    break
                res = min(res, abs(target - ans))
        return res
