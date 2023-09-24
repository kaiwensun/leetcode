from collections import Counter

class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(cnt, prev, path, res):
            if len(cnt) == 1:
                key, value = cnt.items()[0]
                if key != prev:
                    res.append(''.join(path) + key * value)
            else:
                for key, value in list(cnt.items()):
                    if key != prev:
                        for taken in xrange(value):
                            path.append(key)
                            cnt[key] -= 1
                            if cnt[key] == 0:
                                del cnt[key]
                            dfs(cnt, key, path, res)
                        cnt[key] += value
                        for _ in xrange(value):
                            path.pop()
            return res
        return dfs(Counter(s), '', [], [])

