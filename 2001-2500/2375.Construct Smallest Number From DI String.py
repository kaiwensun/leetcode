class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def summarize():
            pair = [0, 0]
            for c in pattern:
                if c == 'I':
                    if pair[1]:
                        yield pair
                        pair = [1, 0]
                    else:
                        pair[0] += 1
                else:
                    pair[1] += 1
            yield pair
        mx = 0
        res = [mx] if pattern[0] == 'I' else []
        for i, d in summarize():
            total = i + d
            for n in range(mx + 1, mx + i):
                res.append(n)
            mx += total
            for n in range(mx, mx - d - 1, -1):
                res.append(n)
        mn = min(res)
        res = [str(n + mn + 1) for n in res]
        return ''.join(res)

