class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        posi = dict(map(reversed, enumerate(row)))
        res = 0
        for i in xrange(0, len(row), 2):
            j = i + 1
            while row[i] // 2 != row[j] // 2:
                partner = row[j] ^ 1
                partner_posi = posi[partner]
                swap_posi = partner_posi ^ 1
                row[j], row[swap_posi] = row[swap_posi], row[j]
                res += 1
        return res

