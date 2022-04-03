class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set(m[0] for m in matches) | set(m[1] for m in matches)
        loser_cnt = Counter([m[1] for m in matches])
        return sorted(players - set(loser_cnt.keys())), sorted(k for k, v in loser_cnt.items() if v == 1)

