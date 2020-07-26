class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        counter = collections.Counter(nums)
        nums = list(set(nums))
        def dfs(i, path):
            if i == len(nums):
                res.append(list(path))
            else:
                dfs(i + 1, path)
                for _ in xrange(counter[nums[i]]):
                    path.append(nums[i])
                    dfs(i + 1, path)
                for _ in xrange(counter[nums[i]]):
                    path.pop()
        dfs(0, [])
        return res
