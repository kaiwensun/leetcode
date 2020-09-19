class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        flat_requests = []
        for start, end in requests:
            flat_requests.append((start, 1))
            flat_requests.append((end + 1, -1))
        flat_requests.sort()
        cnt = request_idx = 0
        counter = [None] * len(nums)
        for i in xrange(len(nums)):
            while request_idx < len(flat_requests) and flat_requests[request_idx][0] == i:
                cnt += flat_requests[request_idx][1]
                request_idx += 1
            counter[i] = cnt
        res = 0
        for cnt, num in zip(sorted(counter, reverse=True), sorted(nums, reverse=True)):
            res += cnt * num
            res %= MOD
        return res

