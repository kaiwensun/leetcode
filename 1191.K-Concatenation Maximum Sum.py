class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        def get_leading_neg(arr):
            mn = cur = 0
            for a in arr:
                cur += a
                mn = min(mn, cur)
            return mn

        def max_sum_in_arr(arr):
            mx = cur = 0
            for a in arr:
                cur += a
                if cur < 0:
                    cur = 0
                mx = max(cur, mx)
            return mx

        res = 0
        s = sum(arr)
        MOD = 10**9 + 7
        left_leading_mn = get_leading_neg(arr)
        right_leading_mn = get_leading_neg(arr[::-1])
        mx_sum_in_arr = max_sum_in_arr(arr)
        all_arr = mx_sum_in_arr + s * (k - 1)
        one_arr = mx_sum_in_arr
        two_arr = max_sum_in_arr(arr + arr) if k > 1 else 0
        return max(all_arr, one_arr, two_arr) % MOD
