class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        K = 2
        left = 0
        counter = collections.Counter()
        res = 0
        for right in xrange(len(tree)):
            if counter[tree[right]] == 0:
                K -= 1
            counter[tree[right]] += 1
            while K == -1:
                counter[tree[left]] -= 1
                if counter[tree[left]] == 0:
                    K += 1
                left += 1
            res = max(res, right - left + 1)
        return res
