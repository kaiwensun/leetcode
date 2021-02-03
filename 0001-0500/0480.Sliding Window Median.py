class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        smaller, bigger = [], []
        smaller_debt, bigger_debt = Counter(), Counter()

        INF = float("inf")

        def get_smaller_head():
            while smaller and smaller_debt[-smaller[0]] > 0:
                smaller_debt[-smaller[0]] -= 1
                heapq.heapreplace(smaller, INF)
            return -smaller[0] if smaller else -INF

        def get_bigger_head():
            while bigger and bigger_debt[bigger[0]] > 0:
                bigger_debt[bigger[0]] -= 1
                heapq.heapreplace(bigger, INF)
            return bigger[0] if bigger else INF

        def append(num):
            if num > get_smaller_head():
                heapq.heappush(bigger, num)
            else:
                heapq.heappush(smaller, -num)

        def remove(num):
            sh = get_smaller_head()
            bh = get_bigger_head()
            if sh == num:
                assert(num == -heapq.heappop(smaller))
            elif bh == num:
                assert(num == heapq.heappop(bigger))
            elif num < sh:
                smaller_debt[num] += 1
                heapq.heappush(bigger, INF)
            elif num > bh:
                bigger_debt[num] += 1
                heapq.heappush(smaller, INF)
            else:
                assert(False)

        def get_median():
            while len(smaller) > len(bigger):
                sh = get_smaller_head()
                assert(sh == -heapq.heappop(smaller))
                heapq.heappush(bigger, sh)
            while len(smaller) + 1 < len(bigger):
                bh = get_bigger_head()
                assert(bh == heapq.heappop(bigger))
                heapq.heappush(smaller, -bh)
            if (len(smaller) + len(bigger)) % 2:
                return get_bigger_head()
            else:
                return (get_bigger_head() + get_smaller_head()) / 2.0

        res = []
        for i in xrange(len(nums)):
            append(nums[i])
            if i >= k - 1:
                res.append(get_median())
                remove(nums[i - k + 1])
        return res

