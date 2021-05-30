class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def translate(s):
            return int("".join(str(ord(c) - ord('a')) for c in s))
        return translate(firstWord) + translate(secondWord) == translate(targetWord)

