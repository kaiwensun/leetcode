class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        sumB = sum(B)
        setA = set(A)
        setB = set(B)
        for a in setA:
            if (sumB - sumA) / 2 + a in setB:
                return [a, (sumB - sumA) / 2 + a]
