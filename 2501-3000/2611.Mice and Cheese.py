class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diff = sorted(enumerate(r1 - r2 for r1, r2 in zip(reward1, reward2)), key=lambda iv:-iv[1])
        m1 = set(iv[0] for iv in diff[:k])
        res = 0
        for i in range(len(reward1)):
            res += reward1[i] if i in m1 else reward2[i]
        return res

