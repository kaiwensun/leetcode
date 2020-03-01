import collections
class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        counter = collections.defaultdict(lambda: [0] * len(votes[0]))
        for vote in votes:
            for posi, team in enumerate(vote):
                counter[team][posi] -= 1
        arr = [score + [team] for team, score in counter.iteritems()]
        arr = sorted(arr)
        return "".join([score[-1] for score in arr])
