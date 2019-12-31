class Solution(object):
    def numSimilarGroups(self, words):
        """
        :type A: List[str]
        :rtype: int
        """
        words = list(set(words))
        data = range(len(words))
        def find(x):
            if x != data[x]:
                data[x] = find(data[x])
            return data[x]
        def union(x, y):
            if find(x) != find(y):
                data[find(x)] = find(y)
        def is_similar(x, y):
            diff_cnt = 0
            c1 = c2 = None
            w1, w2 = words[x], words[y]
            for i in range(len(w1)):
                if w1[i] == w2[i]:
                    continue
                diff_cnt += 1
                if diff_cnt > 2:
                    return False
                elif diff_cnt == 1:
                    c1 = w1[i]
                    c2 = w2[i]
                elif diff_cnt == 2:
                    if c1 != w2[i] or c2 != w1[i]:
                        return False
            return diff_cnt in [0, 2]
        for i in xrange(len(words)):
            for j in xrange(i + 1, len(words)):
                if is_similar(i, j):
                    union(i, j)

        return sum(i == data[i] for i in xrange(len(words)))
