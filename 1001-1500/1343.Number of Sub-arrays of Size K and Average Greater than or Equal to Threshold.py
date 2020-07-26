class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        res, s = 0, sum(arr[: k - 1])
        threshold *= k
        t = k - 1
        for i in xrange(t, len(arr)):
            s += arr[i]
            res += s >= threshold
            s -= arr[i - t]
        return res
