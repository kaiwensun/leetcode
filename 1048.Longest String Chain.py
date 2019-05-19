class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        len2words = collections.defaultdict(list)
        for word in words:
            len2words[len(word)].append(word)
        longestFollow = {}
        def isPre(w1, w2):
            # assume len(w1) + 1 == len(w2)
            for i in xrange(len(w1)):
                if w1[i] != w2[i]:
                    return w1[i:] == w2[i + 1:]
            return True
        def getLongest(word):
            if word is None:
                return 0
            if word not in longestFollow:
                mx_cnt = 0
                for follow in len2words[len(word) + 1]:
                    if isPre(word, follow):
                        cnt = getLongest(follow)
                        mx_cnt = max(mx_cnt, cnt)
                longestFollow[word] = mx_cnt + 1
            return longestFollow[word]
        cnt = 0
        for word in words:
            cnt = max(cnt, getLongest(word))
        return cnt
