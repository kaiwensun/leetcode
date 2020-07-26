from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        target = Counter(words)
        if not words:
            return result
        K = len(words[0])
        counter = Counter()
        for offset in xrange(0, K):
            start = r = offset
            counter.clear()
            while r < len(s):
                word = s[r: r + K]
                if word in target and counter[word] < target[word]:
                    counter[word] += 1
                    if counter[word] == target[word]:
                        if (r - start) / K == len(words) - 1:
                            result.append(start)
                            counter[s[start: start + K]] -= 1
                            start += K
                elif word in target and counter[word] == target[word]:
                    while counter[word] == target[word]:
                        counter[s[start: start + K]] -= 1
                        start += K
                    r -= K
                else:
                    start = r + K
                    counter.clear()
                r += K
        return result
                
                
