class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = 0
        letters = []
        numbers = []
        for c in s:
            if ord('a') <= ord(c) <= ord('z'):
                letters.append(c)
            else:
                numbers.append(c)
        if -1 <= len(letters) - len(numbers) <= 1:
            if len(letters) < len(numbers):
                letters, numbers = numbers, letters
            res = []
            for i in xrange(len(numbers)):
                res.append(letters[i])
                res.append(numbers[i])
            if len(letters) > len(numbers):
                res.append(letters[-1])
            return "".join(res)
        else:
            return ""
