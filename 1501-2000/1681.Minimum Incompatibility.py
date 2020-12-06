from itertools import combinations
from collections import defaultdict
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        unselected_indexes = defaultdict(list)
        for i, num in enumerate(nums):
            unselected_indexes[num].append(i)

        EACH_GROUP_SIZE = len(nums) // k
        
        @lru_cache(None)
        def select_group(pregroup_selected_bits):
            if pregroup_selected_bits == (1 << len(nums)) - 1:
                return 0
            res = float("inf")
            for selected_nums in combinations([num for num, lst in unselected_indexes.items() if len(lst) != 0], EACH_GROUP_SIZE):
                indexes = []
                selected_bits = 0
                for selected_num in selected_nums:
                    index = unselected_indexes[selected_num].pop()
                    selected_bits |= 1 << index
                    indexes.append(index)
                compability = max(selected_nums) - min(selected_nums)
                res = min(res, compability + select_group(pregroup_selected_bits | selected_bits))
                for selected_num, index in zip(selected_nums, indexes):
                    unselected_indexes[selected_num].append(index)
            return res
        res = select_group(0)
        return -1 if res == float("inf") else res

