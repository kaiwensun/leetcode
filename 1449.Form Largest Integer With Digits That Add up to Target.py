from functools import lru_cache
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        cost2num = {}
        for i, c in enumerate(cost):
            cost2num[c] = max(cost2num.get(c, 0), i + 1)
        sorted_num_cost = list(sorted(((str(num), cost) for (cost, num) in cost2num.items()), reverse=True))
        
        @lru_cache(None)
        def dp(length, target):
            """
            Use `target` cost to construct the biggest number of length `length`.
            If it is impossible to construct, return None
            """
            if length <= 0 or target <= 0:
                return "" if length == target == 0 else None
            if min_cost * length > target or max_cost * length < target:
                return None
            for num, cost in sorted_num_cost:
                res = dp(length - 1, target - cost)
                if res is not None:
                    return num + res
                
        min_cost = min(cost2num.keys())
        max_cost = max(cost2num.keys())
        max_length = min(target // min_cost + 1, target)
        candidates = [dp(length, target) for length in range(1, max_length + 1)] + ["0"]
        candidates = [item for item in candidates if item is not None]
        max_len = max(map(len, candidates))
        return max("".join(item) for item in candidates if len(item) == max_len)
        
