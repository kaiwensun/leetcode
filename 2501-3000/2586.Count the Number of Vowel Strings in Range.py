class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        aeiou = "aeiou"
        return len([word for word in words[left : right + 1] if word[0] in aeiou and word[-1] in aeiou])

