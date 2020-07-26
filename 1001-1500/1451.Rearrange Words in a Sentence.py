class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        return " ".join(t[1].lower() for t in sorted(enumerate(text.split(" ")), cmp=lambda a, b: len(a[1]) - len(b[1]) or a[0] - b[0])).capitalize()
