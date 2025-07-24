from sortedcontainers import SortedSet
import collections

class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def popcount_depth(x):
            res = 0
            while x != 1:
                x = str(bin(x)).count("1")
                res += 1
            return res

        # a groups[k] is a SortedSet that contains the indexes i such that popcount_depth(nums[i]) == k
        groups = collections.defaultdict(SortedSet)
        depths = [popcount_depth(x) for x in nums]
        index_to_k = [0] * len(nums)
        for i, k in enumerate(depths):
            index_to_k[i] = k
            groups[k].add(i)
        answer = []
        for query in queries:
            match query[0]:
                case 1:
                    _, l, r, k = query
                    if k not in groups:
                        answer.append(0)
                        continue
                    cnt_le_r = groups[k].bisect_right(r)
                    cnt_l_l = groups[k].bisect_left(l)
                    answer.append(cnt_le_r - cnt_l_l)
                case 2:
                    _, idx, val = query
                    new_k = popcount_depth(val)
                    old_k = index_to_k[idx]
                    if old_k == new_k:
                        continue
                    groups[old_k].remove(idx)
                    index_to_k[idx] = new_k
                    groups[new_k].add(idx)
        return answer

