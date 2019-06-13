class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        counter = collections.Counter(text)
        seen = set()
        stack = []
        for c in text:
            counter[c] -= 1
            if c in seen:
                continue
            seen.add(c)
            while stack and stack[-1] > c and counter[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(c)
        return ''.join(stack)
