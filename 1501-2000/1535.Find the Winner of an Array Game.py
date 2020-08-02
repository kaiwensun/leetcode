class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if k >= len(arr):
            return max(arr)
        win = -1
        mx_num = arr[0]
        for i, a in enumerate(arr):
            if a > mx_num:
                mx_num = a
                win = 0
            win += 1
            print('?',i, win)
            if win >= k:
                break
        return mx_num
