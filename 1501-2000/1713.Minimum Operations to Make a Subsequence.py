class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        inversed = dict(map(reversed, enumerate(target)))
        arr = [inversed[item] for item in arr if item in inversed]
        inc = []
        for item in arr:
            index = bisect.bisect_left(inc, item)
            if index == len(inc):
                inc.append(item)
            else:
                inc[index] = item
        return len(target) - len(inc)

