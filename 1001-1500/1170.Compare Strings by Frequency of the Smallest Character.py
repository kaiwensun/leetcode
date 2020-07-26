class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        def f(w):
            return min(collections.Counter(w).iteritems())[1]
        f_words = sorted(map(f, words))
        res = [0] * len(queries)
        for i in xrange(len(queries)):
            f_query = f(queries[i])
            res[i] = len(words) - bisect.bisect_right(f_words, f_query)
        return res
