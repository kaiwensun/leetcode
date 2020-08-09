from collections import defaultdict
class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        prefix2index = defaultdict(list)
        prefix2index[0].append(-1)
        index2bestRes = [0] * len(nums)
        sm = 0
        for i, num in enumerate(nums):
            sm += num
            wanted = sm - target
            res = max(index2bestRes[j] for j in prefix2index[wanted]) + 1 if prefix2index[wanted] else 0
            index2bestRes[i] = max(res, index2bestRes[i - 1])
            prefix2index[sm].append(i)
        return index2bestRes[-1]
