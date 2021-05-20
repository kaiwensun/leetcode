from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        return [item[0] for item in heapq.nsmallest(k, Counter(words).items(), key=lambda item: (-item[1], item[0]))]

