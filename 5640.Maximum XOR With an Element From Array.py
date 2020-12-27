from collections import defaultdict
class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nums.sort()
        T = lambda: defaultdict(T)
        trie = T()
        sorted_queries = [[q[1], q[0], i] for i, q in enumerate(queries)]
        sorted_queries.sort()  # [m, x, i]
        answer = []
        
        def put(p, i, bnum):
            p = p[(bnum >> i) & 1]
            if i == 0:
                p["#"] = bnum
            else:
                put(p, i - 1, bnum)
        def que(p, i, x):
            if i == -1:
                return p["#"]
            opt = 1 - ((x >> i) & 1)
            return que(p[opt] if opt in p else p[1 - opt], i - 1, x)

        num_p = 0
        for m, x, i in sorted_queries:
            while num_p < len(nums) and nums[num_p] <= m:
                put(trie, 30, nums[num_p])
                num_p += 1
            answer.append((i, que(trie, 30, x) ^ x if len(trie) else -1))
        return [item[1] for item in sorted(answer)]

