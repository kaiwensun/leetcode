import bisect

MOD = 10 ** 9 + 7

class Solution(object):
    def minWastedSpace(self, packages, suppliers):
        """
        :type packages: List[int]
        :type suppliers: List[List[int]]
        :rtype: int
        """
        packages.sort()
        prefix = [0] + packages
        for i in xrange(len(packages)):
            prefix[i + 1] += prefix[i]

        res = float("inf")
        for boxes in suppliers:
            last_packed_index = 0
            wasted = 0
            for box in sorted(boxes):
                index = bisect.bisect_right(packages, box, lo=last_packed_index)
                wasted += box * (index - last_packed_index) - (prefix[index] - prefix[last_packed_index])
                last_packed_index = index
                if last_packed_index == len(packages):
                    res = min(res, wasted)
                    break
        return -1 if res == float("inf") else (res % MOD)

