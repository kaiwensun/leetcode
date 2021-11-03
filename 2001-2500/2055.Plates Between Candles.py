import bisect

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [i for i, c in enumerate(s) if c == "|"]
        def process(query):
            l, r = query
            l_index = bisect.bisect_left(candles, l)
            r_index = bisect.bisect_right(candles, r) - 1
            return candles[r_index] - candles[l_index] - r_index + l_index if l_index < r_index else 0
        return list(map(process, queries))

