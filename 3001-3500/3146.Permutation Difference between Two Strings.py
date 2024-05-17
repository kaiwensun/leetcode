class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        arr1 = sorted((c, i) for i, c in enumerate(s))
        arr2 = sorted((c, i) for i, c in enumerate(t))
        return sum(abs(a[1] - b[1]) for (a, b) in zip(arr1, arr2))

