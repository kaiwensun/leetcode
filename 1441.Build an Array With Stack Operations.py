class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res = []
        pointer = 0
        num = 1
        while num <= n and pointer < len(target):
            if target[pointer] == num:
                res.append("Push")
                pointer += 1
                num += 1
            else:
                res.append("Push")
                res.append("Pop")
                num += 1
        return res
