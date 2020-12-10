from collections import Counter
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        senate = list(senate)
        alives = Counter(senate)
        to_be_killed = Counter()
        while True:
            for i, player in enumerate(senate):
                if player is None:
                    continue
                enemy = "R" if player == "D" else "D"
                if to_be_killed[player] > 0:
                    to_be_killed[player] -= 1
                    senate[i] = None
                    continue
                if alives[enemy] > 0:
                    alives[enemy] -= 1
                    to_be_killed[enemy] += 1
                else:
                    return "Radiant" if player == "R" else "Dire"

