class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        result = []
        def calc(path):
            buff = []
            for i in range(len(num)):
                buff.append(path[i])
                buff.append(num[i])
            expression = ''.join(buff[1:])
            if eval(expression) == target:
                result.append(expression)

        def dfs(path):
            if len(path) == len(num):
                calc(path)
            else:
                if path[-1] != '' and num[len(path) - 1] == '0':
                    ops = "*+-"
                else:
                    ops = ["", "*", "+", "-"]
                for op in ops:
                    path.append(op)
                    dfs(path)
                    path.pop()

        dfs(["+"])
        return result

