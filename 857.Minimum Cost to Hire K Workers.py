class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        ratio = [(float(wage[i]) / quality[i], i) for i in xrange(len(wage))]
        ratio.sort()
        global_ratio = ratio[K - 1][0]
        global_payment = sum([quality[ratio[i][1]] for i in xrange(K)]) * ratio[K - 1][0]
        neg_cur_employees_quality = [-quality[ratio[i][1]] for i in xrange(K)]
        heapq.heapify(neg_cur_employees_quality)
        min_payment = global_payment
        print ratio
        print global_payment
        print global_ratio
        for i in xrange(K, len(ratio)):
            r = ratio[i]
            global_quality = global_payment / global_ratio
            old_quality = -heapq.heapreplace(neg_cur_employees_quality, -quality[r[1]])
            global_quality = global_quality - old_quality + quality[r[1]]
            global_ratio = r[0]
            global_payment = global_quality * global_ratio
            min_payment = min(min_payment, global_payment)
        return min_payment
