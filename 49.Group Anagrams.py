#Result:
# 100 / 100 test cases passed.
# Status: Accepted
# Runtime: 239 ms
# We are in the progress of updating the graph distribution. Please check the distribution again within weeks.
#Date:
# 9/13/2016

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """ 
        rtn = {}
        for str in strs:
            code = "".join(sorted(str))
            if code not in rtn:
                rtn[code]=list()
            rtn[code].append(str)
        return rtn.values()
