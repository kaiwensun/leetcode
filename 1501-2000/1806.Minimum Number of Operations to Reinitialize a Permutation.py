class Solution:
    def reinitializePermutation(self, n: int) -> int:
        arr = list(range(n))
        arr2 = list(arr)
        t = 1
        arr2 = arr2[0::2] + arr2[1::2]
        while arr != arr2:
                t += 1
                arr2 = arr2[0::2] + arr2[1::2]
        return t

