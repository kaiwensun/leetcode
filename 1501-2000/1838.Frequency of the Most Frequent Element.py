from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        arr = list(map(list, sorted(Counter(nums).items())))
        cohort = res = arr[0][1]
        budget = k
        l = 0
        for r in range(1, len(arr)):
            budget -= cohort * (arr[r][0] - arr[r - 1][0])
            cohort += arr[r][1]
            while budget < 0:
                distance = arr[r][0] - arr[l][0]
                diff = min(arr[l][1], int(math.ceil((-budget) / distance)))
                arr[l][1] -= diff
                cohort -= diff
                budget += diff * distance
                if arr[l][1] == 0:
                    l += 1
            res = max(res, cohort)
        return res

