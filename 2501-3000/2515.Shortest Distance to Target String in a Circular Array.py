class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        res = float("inf")
        for i in range(n):
            if words[i] == target:
                res = min(res, abs(i - startIndex), n - abs(i - startIndex))
        return -1 if res == float("inf") else res

