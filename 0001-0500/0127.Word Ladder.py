from collections import defaultdict, deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        def getNeighbors(word):
            for bucket in getBuckets(word):
                for neighbor in buckets[bucket]:
                    if neighbor != word:
                        yield neighbor
                
        def getBuckets(word):
            for i in xrange(len(word)):
                yield word[:i] +"_" + word[i + 1:]

        if endWord not in wordList:
            return 0
        try:
            wordList.remove(beginWord)
        except ValueError:
            pass
        buckets = defaultdict(list)
        for word in wordList:
            for bucket in getBuckets(word):
                buckets[bucket].append(word)
        seen = {beginWord}
        queue = deque((beginWord, "#"))
        res = 2
        while len(queue) > 1:
            word = queue.popleft()
            if "#" == word:
                queue.append("#")
                res += 1
                continue
            for neighbor in getNeighbors(word):
                if neighbor == endWord:
                    return res
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return 0

