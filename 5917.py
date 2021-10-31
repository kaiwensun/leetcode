from functools import cache

class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:

        @cache
        def dp(i, j, bet):
            if i == -1 and j == -1:
                return bet == 0
            if bet == 0:
                if i == -1 or j == -1:
                    return False
                if s1[i].isalpha() and s2[j].isalpha() and s1[i] == s2[j]:
                    return dp(i - 1, j - 1, bet)
            elif bet > 0:
                if j == -1:
                    return False
                if s2[j].isalpha():
                    return dp(i, j - 1, bet - 1)
            else:  # bet < 0
                if i == -1:
                    return False
                if s1[i].isalpha():
                    return dp(i - 1, j, bet + 1)
            k = i
            while k >= 0 and s1[k].isdigit():
                new_bet = int(s1[k : i + 1])
                if dp(k - 1, j, bet + new_bet):
                    return True
                k -= 1
            k = j
            while k >= 0 and s2[k].isdigit():
                recover_bet = int(s2[k : j + 1])
                if dp(i, k - 1, bet - recover_bet):
                    return True
                k -= 1
            return False
        return dp(len(s1) - 1, len(s2) - 1, 0)

