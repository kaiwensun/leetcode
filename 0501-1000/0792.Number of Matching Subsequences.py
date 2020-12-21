class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        N = len(words)
        trackers = [0] * len(words)
        buckets = [[]for _ in xrange(26)]
        for i in xrange(N):
            buckets[ord(words[i][0]) - ord('a')].append(i)
        res = 0
        for c in S:
            candidates = buckets[ord(c) - ord('a')]
            buckets[ord(c) - ord('a')] = []
            for i in candidates:
                trackers[i] += 1
                if trackers[i] != len(words[i]):
                    buckets[ord(words[i][trackers[i]]) - ord('a')].append(i)
        return len(words) - sum(map(len, buckets))

