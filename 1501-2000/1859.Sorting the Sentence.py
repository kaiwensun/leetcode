class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join(word for (_, word) in sorted((word[-1], word[:-1]) for word in s.split()))

