import functools

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        @functools.lru_cache(None)
        def dp(i, available):
            if i == n:
                print(f"dp({i}, {bin(available)}) => {0}")
                return 0
            res = float("inf")
            for j in range(n):
                if available & (1 << j):
                    res = min(res, (nums1[i] ^ nums2[j]) + dp(i + 1, available ^ (1 << j)))
            return res
        
        return dp(0, (1 << n) - 1)

