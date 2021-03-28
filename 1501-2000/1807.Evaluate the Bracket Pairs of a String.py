class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = dict(knowledge)
        s = s.replace("(", ")").split(")")
        res = []
        for i in range(len(s)):
            if i % 2 == 0:
                res.append(s[i])
            else:
                res.append(knowledge.get(s[i], "?"))
        return "".join(res)

