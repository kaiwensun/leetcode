class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for word in words:
            for c in word:
                if i == len(s) or c != s[i]:
                    return False
                i += 1
            if i == len(s):
                return True
        return False

