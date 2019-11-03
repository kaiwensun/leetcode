from collections import Counter
class Leaderboard(object):

    def __init__(self):
        self.cnt = Counter()
        

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        self.cnt[playerId] += score
        

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        return sum(score for _, score in self.cnt.most_common(K))
        

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        self.cnt[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
