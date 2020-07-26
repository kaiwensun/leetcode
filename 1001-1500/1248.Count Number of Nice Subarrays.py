class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        buff = []
        cnt = 0
        for i, n in enumerate(nums):
            if n % 2 == 0:
                cnt += 1
            else:
                buff.append(cnt)
                cnt = 0
        buff.append(cnt)
        l = 0
        r = l + k
        res = 0
        print buff
        while r < len(buff):
            res += (buff[l] + 1) * (buff[r] + 1)
            l += 1
            r += 1
        return res
