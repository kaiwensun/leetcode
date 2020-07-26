class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ctr_s = collections.Counter(s)
        ctr_t = collections.Counter(t)
        return (ctr_t - ctr_s).most_common(1)[0][0]
