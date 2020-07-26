class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = sorted([num, i] for i, num in enumerate(nums))
        i = 0
        for i in xrange(len(arr)):
            if i == 0 or arr[i][0] != arr[i - 1][0]:
                arr[i].append(i)
            else:
                arr[i].append(arr[i - 1][-1])
        res = sorted((i, cnt) for num, i, cnt in arr)
        return [ele[1] for ele in res]
