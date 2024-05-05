MOD = 10 ** 9 + 7

class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            return ((max(nums) - min(nums)) * cost1) % MOD
        mx = max(nums)
        mn = min(nums)
        if mx == mn:
            return 0
        slots = n * mx - sum(nums)
        res = cost1 * slots
        too_deep = True
        if slots % 2 == 0:
            # if cost2 only can flaten the deepest bar to level mx
            if mx - mn <= slots - (mx - mn):
                res = min(res, slots // 2 * cost2)
                too_deep = False
        else:
            # if multiple cost2 with only one cost1 can flaten the deepest bar to level mx
            if mx - 1 - mn <= slots - (mx - mn):
                res = min(res, slots // 2 * cost2 + cost1)
                too_deep = False
            # if adding an additional row to make slots an even number can help flatten the bars at mx + 1 with only cost2
            if n % 2 == 1:
                if mx + 1 - mn <= slots + n - (mx + 1 - mn):
                    res = min(res, (slots + n) // 2 * cost2)
                    too_deep = False
        if too_deep:
            res_tmp = (slots - (mx - mn)) * cost2
            lowest = mn + (slots - (mx - mn))
            top = mx
            res = min(res, res_tmp + (top - lowest) * cost1)
            while lowest + (n - 1) <= top + 1:
                top += 1
                lowest += n - 1
                res_tmp += (n - 1) * cost2
                res = min(res, res_tmp + (top - lowest) * cost1)
            remain = top - lowest + n
            res = min(res, res_tmp + remain // 2 * cost2 + (cost1 if remain % 2 else 0))
            remain += n
            res = min(res, res_tmp + remain // 2 * cost2 + (cost1 if remain % 2 else 0))
        return res % MOD

