class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed = set(allowed)
        return sum(int(set(word).issubset(allowed)) for word in words)

