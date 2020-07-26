class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        res = [None] * len(barcodes)
        i = 0
        for code, cnt in collections.Counter(barcodes).most_common():
            j = i
            while cnt > 0:
                res[j] = code
                j += 2
                if j >= len(res):
                    j = 1
                cnt -= 1
            i = j
        return res
