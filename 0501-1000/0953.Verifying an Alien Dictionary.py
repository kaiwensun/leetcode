class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dictionary = self.build_dict(order)
        for i in xrange(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            length = min(len(word1), len(word2))
            for j in xrange(length):
                order1 = dictionary[word1[j]]
                order2 = dictionary[word2[j]]
                if order1 > order2:
                    return False
                if order1 < order2:
                    break
                if j == length - 1:
                    if len(word1) > len(word2):
                        return False    
        return True
            
    def build_dict(self, order):
        dictionary = {}
        for i in xrange(len(order)):
            dictionary[order[i]] = i
        return dictionary

