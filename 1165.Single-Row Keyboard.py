class Solution(object):
    def calculateTime(self, keyboard, word):
        dic = dict(map(reversed, enumerate(keyboard)))
        posi = map(dic.__getitem__, word)
        return sum(map(
            lambda (a, b): abs(a - b),
            zip(posi, [0] + posi[:-1])
        ))
