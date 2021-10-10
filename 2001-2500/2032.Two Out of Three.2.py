class Solution(object):
    def twoOutOfThree(self, *nums_list):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        res = []
        for num, cnt in sum(map(Counter, map(set, nums_list)), Counter()).iteritems():
            if cnt >= 2:
                res.append(num)
        return res

