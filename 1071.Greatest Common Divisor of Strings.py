import fractions
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        gcd = fractions.gcd(len(str1), len(str2))
        if str1[:gcd] == str2[:gcd]:
            return str1[:gcd]
        return ''
