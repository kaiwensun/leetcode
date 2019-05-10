class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = collections.Counter(nums)
        res = []
        if counter[0] >= 3:
            res.append([0] * 3)
        keys = sorted(counter.keys())
        print keys
        for i in xrange(len(keys)):
            x = keys[i]
            if counter[x] >= 2 and -x - x in counter and x < 0:
                res.append([x, x, -x -x])
            for j in xrange(i + 1, len(keys)):
                y = keys[j]
                z = -x -y
                if y == z:
                    if counter[y] >= 2:
                        res.append([x, y, z])
                elif y < z:
                    if z in counter:
                        res.append([x, y, z])
        return res
