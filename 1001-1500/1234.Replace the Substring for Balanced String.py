from collections import Counter, deque, defaultdict
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """

        KEYS = "QWER"
        extra = Counter(s)
        for c in KEYS:
            extra[c] -= len(s) // 4
            if extra[c] <= 0:
                del extra[c]
        if not extra:
            return 0
        KEYS = "".join(extra.keys())
        queues = defaultdict(deque)
        res = float("inf")
        extra_sm = sum(extra.values())
        for i, c in enumerate(s):
            if c not in KEYS:
                continue
            queues[c].append(i)
            if len(queues[c]) > extra[c]:
                queues[c].popleft()
            if sum(map(len, queues.values())) == extra_sm:
                res = min(res, i - min(queue[0] for queue in queues.values()))
        return res + 1

