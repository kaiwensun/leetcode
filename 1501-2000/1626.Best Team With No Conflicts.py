class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        players = list(sorted(zip(ages, scores)))
        dp = [0] * len(players)
        for youngest in xrange(len(players) - 1, -1, -1):
            dp[youngest] = players[youngest][1] + max([dp[i] for i in xrange(youngest + 1, len(players)) if players[youngest][1] <= players[i][1]] + [0])
        return max(dp)

