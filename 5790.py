from collections import Counter
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        prefix = []
        cnt = Counter()
        for num in nums:
            cnt[num] += 1
            prefix.append(Counter(cnt))
        prefix.append(Counter())
        ans = []
        for l, r in queries:
            sorted_cnt = sorted((prefix[r] - prefix[l - 1]).items())
            res = float("inf")
            for i in range(len(sorted_cnt) - 1):
                res = min(res, sorted_cnt[i + 1][0] - sorted_cnt[i][0])
            res = -1 if res == float("inf") else res
            ans.append(res)
        return ans

