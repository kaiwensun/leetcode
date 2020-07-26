import bisect

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        p2index = {}
        heap = []
        self.times = []
        self.time2p = {}
        sorted_time_person = sorted(zip(times, persons))
        for time, person in sorted_time_person:
            if person in p2index:
                index = p2index[person]
                heap[index][0] += 1
            else:
                index = p2index[person] = len(heap)
                heap.append([1, person])
            while index != 0 and heap[(index - 1) / 2][0] <= heap[index][0]:
                parent = (index - 1) / 2
                p2index[person] = parent
                p2index[heap[parent][1]] = index
                heap[index], heap[parent] = heap[parent], heap[index]
                index = parent
            leader = heap[0][1]
            if not self.times or self.times[-1] != time:
                self.times.append(time)
            self.time2p[time] = leader


    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        index = bisect.bisect_right(self.times, t) - 1
        time = self.times[index]
        return self.time2p[time]
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
