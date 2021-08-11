from collections import Counter, defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = defaultdict(Counter)  # ending_num => diff => count
        single = defaultdict(Counter)  # ending_num => diff => count
        for i, num in enumerate(nums):
            new_res = Counter()
            for prev in res, single:
                for ending_num, counter in prev.items():
                    diff = num - ending_num
                    if diff in counter:
                        new_res[diff] += counter[diff]
            for j in range(i):
                single[nums[i]][num - nums[j]] += 1
            res[num] += new_res
        return sum(sum(counter.values()) for counter in res.values())

