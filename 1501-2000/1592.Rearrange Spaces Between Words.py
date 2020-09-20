from collections import Counter
class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        cnt = Counter(text)
        words = [word for word in text.split(" ") if word]
        if len(words) == 1:
            return words[0] + " " * cnt[" "]
        return (" " * (cnt[" "] // (len(words) - 1))).join(words) + " " * (cnt[" "] % (len(words) - 1))

