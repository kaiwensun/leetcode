class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        i, j = 0, len(tokens) - 1
        points = 0
        rval = 0
        power = P
        while i <= j:
            while i <= j and tokens[i] <= power:
                points += 1
                rval = max(rval, points)
                power -= tokens[i]f
                i += 1
            if points and i <= j:
                points -= 1
                power += tokens[j]
                j -= 1
            else:
                break
        return points
