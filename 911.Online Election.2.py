import bisect
import collections

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        counter = collections.Counter()
        winner = None
        sorted_time_person = sorted(zip(times, persons))
        self.time2person = {}
        self.times = []
        for time, person in sorted_time_person:
            if not self.times or self.times[-1] != time:
                self.times.append(time)
            counter[person] += 1
            if counter[person] >= counter[winner]:
                winner = person
            self.time2person[time] = winner

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        index = bisect.bisect_right(self.times, t) - 1
        time = self.times[index]
        return self.time2person[time]
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
