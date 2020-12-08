class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_comment = False
        comment_start = ["//", "/*"]
        def tokenize(line):
            nonlocal in_comment
            i = 0
            while i < len(line):
                if in_comment:
                    if line[i : i + 2] == "*/":
                        in_comment = False
                        i += 2
                    else:
                        i += 1
                elif line[i : i + 2] in comment_start:
                    if line[i : i + 2] == "//":
                        break
                    else:
                        in_comment = True
                        i += 2
                else:
                    yield line[i]
                    i += 1

        res = []
        res_line = []
        for line in source:
            for token in tokenize(line):
                res_line.append(token)
            if not in_comment and res_line:
                res.append("".join(res_line))
                res_line = []
        return res

