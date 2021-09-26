from functools import cache

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        score = 0
        correct = eval(s)
        s = [int(c) if c not in "+*" else (int.__mul__ if c == '*' else int.__add__) for c in s]

        @cache
        def dp(i, j):
            if i + 1 == j:
                return {s[i]}
            res = set()
            for split in range(i + 1, j, 2):
                lset = dp(i, split)
                rset = dp(split + 1, j)
                for l in lset:
                    for r in rset:
                        num = s[split](l, r)
                        if num <= 1000:
                            res.add(num)
            return res

        incorrect = dp(0, len(s))     
        for answer in answers:
            if answer == correct:
                score += 5
            elif answer in incorrect:
                score += 2
        dp.cache_clear()
        return score

