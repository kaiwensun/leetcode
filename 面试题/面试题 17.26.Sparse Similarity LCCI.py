from decimal import Decimal

class Solution(object):
    def computeSimilarities(self, docs):
        """
        :type docs: List[List[int]]
        :rtype: List[str]
        """
        def get_bits(doc):
            res = 0
            for num in doc:
                res |= 1 << num
            return res
        def count_overlap(bit1, bit2):
            bit_xor = bit1 ^ bit2
            bit_or = bit1 | bit2
            diff = bit_or - bit_xor
            res = 0
            while diff:
                diff &= diff - 1
                res += 1
            return res

        bits = map(get_bits, docs)
        res = []
        for i in xrange(len(docs)):
            for j in xrange(i + 1, len(docs)):
                overlap = count_overlap(bits[i], bits[j])
                if overlap != 0:
                    union = len(docs[i]) + len(docs[j]) - overlap
                    if overlap == union:
                        similarity = "1.0000"
                    else:
                        similarity = overlap * 100000 // union
                        if similarity % 10 < 5:
                            similarity //= 10
                        else:
                            similarity //= 10
                            similarity += 1
                        similarity = "0.%04d" % similarity
                    res.append("%d,%d: %s" % (i, j, similarity))
        return res

