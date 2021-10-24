class Solution:
    def countValidWords(self, sentence: str) -> int:
        res = 0

        def test(word):
            if word[-1].isdigit() or word[-1] == '-':
                return False
            for i, c in enumerate(word[:-1]):
                if not ('a' <= c <= 'z' or c == '-'):
                    return False
            hyphon = word.find('-')
            if hyphon != -1:
                if word.count('-') > 1:
                    return False
                if hyphon == 0 or hyphon == len(word) - 1:
                    return False
            if word[-1] in '!,.':
                if len(word) > 1 and word[-2] == '-':
                    return False
            return True

        return sum(map(test, sentence.split()))

