from collections import Counter
import string

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        for c in string.ascii_lowercase:
            cnt1[c] = cnt1[c]
            cnt2[c] = cnt2[c]
        for c1 in string.ascii_lowercase:
            if cnt1[c1] == 0:
                continue
            cnt1[c1] -=1
            cnt2[c1] += 1
            for c2 in string.ascii_lowercase:
                if cnt2[c2] == 0:
                    continue
                if c1 == c2 and cnt2[c2] == 1:
                    continue
                cnt1[c2] += 1
                cnt2[c2] -= 1
                if len([k for k, v in cnt1.items() if v]) == len([k for k, v in cnt2.items() if v]):
                    return True
                cnt1[c2] -= 1
                cnt2[c2] += 1
            cnt1[c1] +=1
            cnt2[c1] -= 1
        return False

