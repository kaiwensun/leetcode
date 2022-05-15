class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            if res and sorted(res[-1]) == sorted(word):
                continue
            res.append(word)
        return res

