class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = map(lambda cnt: (cnt["0"], cnt["1"]), map(Counter, strs))

        cases = Counter()
        for cnt in cnts:
            new_cases = Counter()
            if cnt[0] <= m and cnt[1] <= n:
                new_cases[cnt] = 1
            for case, card in cases.items():
                key = (case[0] + cnt[0], case[1] + cnt[1])
                if key[0] > m or key[1] > n:
                    continue
                new_cases[key] = max(new_cases[key], card + 1)
            for new_case, card in new_cases.items():
                cases[new_case] = max(cases[new_case], card)
        return max(cases.values()) if cases else 0

