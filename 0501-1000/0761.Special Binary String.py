class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        def get_consecutive_substrings(S, start):
            zeros = ones = 0
            anchor = start
            res = []
            for i in xrange(start, len(S)):
                if S[i] == "0":
                    zeros += 1
                else:
                    ones += 1
                if zeros > ones:
                    break
                if zeros == ones and zeros != 0:
                    res.append(S[anchor:i + 1])
                    anchor = i + 1
                    ones = zeros = 0
            return res

        changed = True
        while changed:
            changed = False
            for start in xrange(len(S)):
                substrings = get_consecutive_substrings(S, start)
                total_size = sum(map(len, substrings))
                substrings.sort(reverse=True)
                if len(substrings) > 1:
                    new_substr = [item for substring in substrings for item in substring]
                    if S[start:start+total_size] != new_substr:
                        changed = True
                        S[start:start+total_size] = new_substr

        return "".join(S)

