class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        i = 0
        while i < len(A):
            if A[i] == i + 1:
                i += 1
            else:
                result.extend(self.swap(i, A[i] - 1, A))
                
        return result
        
    def swap(self, index1, index2, A):
        A[index1], A[index2] = A[index2], A[index1]
        i = min(index1, index2) + 1
        j = max(index1, index2) + 1
        if j - i != 1:
            return [j, j - i, j - i - 1, j - i, j - i + 1, j]
        else:
            return [j, j - i + 1, j]

        
        
        
