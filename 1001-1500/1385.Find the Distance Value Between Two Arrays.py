class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr1.sort()
        arr2.sort()
        arr2 = [float('-inf')] + arr2 + [float('inf')]
        j, res = 0, 0
        for i in xrange(len(arr1)):
            while arr2[j + 1] < arr1[i]:
                j += 1
            if arr2[j] + d < arr1[i] < arr2[j + 1] - d:
                res += 1
        return res
