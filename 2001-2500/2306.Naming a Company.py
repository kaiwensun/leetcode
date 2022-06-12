from collections import defaultdict

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        tails = defaultdict(set)
        for idea in ideas:
            first, tail = idea[0], idea[1:]
            tails[first].add(tail)

        firsts = list(tails.keys())
        res = 0
        for i in range(len(firsts)):
            tail1 = tails[firsts[i]]
            for j in range(i + 1, len(firsts)):
                tail2 = tails[firsts[j]]
                res += len(tail1 - tail2) * len(tail2 - tail1)
        return res * 2

