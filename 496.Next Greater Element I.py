class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = {n: i for i, n in enumerate(nums1)}
        rval = [None] * len(nums1)
        stack = []
        for i in xrange(len(nums2) - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if nums2[i] in nums1:
                rval[nums1[nums2[i]]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        return rval
