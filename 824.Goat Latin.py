class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        for i in xrange(len(words)):
            if words[i][0].lower() not in 'aeiou':
                words[i] = words[i][1:] + words[i][:1]
            words[i] += 'ma' + 'a' * (i + 1)
        return ' '.join(words)
