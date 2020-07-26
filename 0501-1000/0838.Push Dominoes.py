class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes = list(dominoes)
        left = (-1, 'L')
        for i in xrange(len(dominoes)):
            if dominoes[i] == 'L':
                if left[1] == 'L':
                    for j in xrange(left[0] + 1, i):
                        dominoes[j] = 'L'
                else:
                    for j in xrange((left[0] + i + 1) / 2, i):
                        dominoes[j] = 'L'
                    if (i - left[0]) % 2 == 0:
                        dominoes[(left[0] + i + 1) / 2] = '.'
                left = (i, 'L')
            elif dominoes[i] == 'R':
                left = (i, 'R')
            else:
                if left[1] == 'R':
                    dominoes[i] = 'R'
        return ''.join(dominoes)
