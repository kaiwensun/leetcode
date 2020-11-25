class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def tokenize(s):
            num = ""
            for c in s:
                if c == " ":
                    continue
                if c in "+-()":
                    if num:
                        yield int(num)
                        num = ""
                    yield c
                else:
                    num += c
            if num:
                yield int(num)
        
        def process(tokenizer):
            res = 0
            op = int.__add__
            token = next(tokenizer)
            while token != ")":
                if token == "(":
                    res = op(res, process(tokenizer))
                elif token == "+":
                    op = int.__add__
                elif token == "-":
                    op = int.__sub__
                else:
                    res = op(res, token)
                token = next(tokenizer)
            return res

        return process(tokenize(s + ")"))

