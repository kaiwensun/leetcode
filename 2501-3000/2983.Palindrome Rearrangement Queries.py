from collections import Counter

MOD = 10 ** 9 + 7


class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s) // 2
        s1 = s[:n]
        s2 = s[-n:][::-1]

        def calc_counters(s):
            cnt = Counter()
            res = [Counter()]
            for c in s:
                cnt[c] += 1
                res.append(Counter(cnt))
            return res

        def calc_rolling_sum(s):
            res = [0]
            sm = 0
            for c in s:
                sm *= 26
                sm += ord(c) - ord('a')
                sm %= MOD
                res.append(sm)
            return res

        cnt1 = calc_counters(s1)
        cnt2 = calc_counters(s2)
        rs1 = calc_rolling_sum(s1)
        rs2 = calc_rolling_sum(s2)

        def normalize(a, b, c, d):
            b = b + 1
            d = 2 * n - d - 1
            c = 2 * n - c
            c, d = d, c
            if a > c:
                return c, d, a, b, cnt2, cnt1, rs2, rs1
            return a, b, c, d, cnt1, cnt2, rs1, rs2

        def rolling_sums_match(rs1, rs2, start, end):
            size = end - start
            shift = pow(26, size, MOD)
            return (rs1[end] - rs1[start] * shift) % MOD == (rs2[end] - rs2[start] * shift) % MOD

        def invalid_cnt(cnt):
            return cnt and min(cnt.values()) < 0

        def minus(cnt1, cnt2):
            cnt = cnt1.copy()
            cnt.subtract(cnt2)
            return cnt

        def calc_query(a, b, c, d):
            a, b, c, d, cnt1, cnt2, rs1, rs2 = normalize(a, b, c, d)
            if not rolling_sums_match(rs1, rs2, 0, a):
                return False
            if not rolling_sums_match(rs1, rs2, max(b, d), n):
                return False
            if c <= b:
                if d <= b:
                    s1_range123 = minus(cnt1[b], cnt1[a])
                    s2_range1 = minus(cnt2[c], cnt2[a])
                    s1_range23 = s1_range123 - s2_range1
                    if invalid_cnt(s1_range23):
                        return False
                    s2_range3 = minus(cnt2[b], cnt2[d])
                    s1_range2 = minus(s1_range23, s2_range3)
                    if invalid_cnt(s1_range2):
                        return False
                    s2_range2 = minus(cnt2[d], cnt2[c])
                    return s1_range2 == s2_range2
                else: # d > b
                    s1_range12 = minus(cnt1[b], cnt1[a])
                    s2_range1 = minus(cnt2[c], cnt2[a])
                    s1_range2 = minus(s1_range12, s2_range1)
                    if invalid_cnt(s1_range2):
                        return False
                    s2_range23 = minus(cnt2[d], cnt2[c])
                    s1_range3 = minus(cnt1[d], cnt1[b])
                    s2_range2 = minus(s2_range23, s1_range3)
                    if invalid_cnt(s2_range2):
                        return False
                    return s1_range2 == s2_range2
            else: # b < c
                if not rolling_sums_match(rs1, rs2, b, c):
                    return False
                if minus(cnt1[b], cnt1[a]) != minus(cnt2[b], cnt2[a]):
                    return False
                if minus(cnt1[d], cnt1[c]) != minus(cnt2[d], cnt2[c]):
                    return False
            return True
        return [calc_query(*query) for query in queries]

