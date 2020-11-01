class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """

        pieces = {piece[0] : piece for piece in pieces if piece}
        i = 0
        while i < len(arr):
            piece = pieces.get(arr[i])
            if not piece:
                return False
            j = 0
            while i < len(arr) and j < len(piece):
                if arr[i] != piece[j]:
                    return False
                i += 1
                j += 1
            if j != len(piece):
                return False
        return True

