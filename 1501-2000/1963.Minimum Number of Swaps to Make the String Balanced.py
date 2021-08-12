class Solution:
    def minSwaps(self, s: str) -> int:
        res = depth = seen_open = 0
        for i, c in enumerate(s):
            if c == '[':
                seen_open += 1
                depth += 1
            else:
                if depth == 0:
                    res += 1
                    seen_open += 1
                    depth += 1
                else:
                    depth -= 1
            if seen_open == len(s) // 2:
                break
        return res

