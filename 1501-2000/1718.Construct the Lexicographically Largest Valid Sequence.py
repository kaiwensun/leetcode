class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        seen = [False] * (n + 1)
        res = [None] * (n * 2 - 1)
        def dfs(i):
            if i == len(res):
                return True
            if res[i]:
                return dfs(i + 1)
            for num in range(n, 1, -1):
                if not seen[num]:
                    if i + num >= len(res):
                        return False
                    if res[i + num]:
                        continue
                    seen[num] = True
                    res[i] = res[i + num] = num
                    if dfs(i + 1):
                        return True
                    res[i] = res[i + num] = None
                    seen[num] = False
            if not seen[1]:
                seen[1] = True
                res[i] = 1
                if dfs(i + 1):
                    return True
                res[i] = None
                seen[1] = False
            return False
        dfs(0)
        return res

