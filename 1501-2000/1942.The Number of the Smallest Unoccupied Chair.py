import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        T = []
        for i, (arrive, leave) in enumerate(times):
            T.append((arrive, True, i))
            T.append((leave, False, i))
        T.sort()
        taken = {}
        available = []
        for t, is_arrive, i in T:
            if is_arrive:
                if available:
                    seat = heapq.heappop(available)
                else:
                    seat = len(taken)
                if i == targetFriend:
                    return seat
                taken[i] = seat
            else:
                heapq.heappush(available, taken[i])
                del taken[i]
        assert(False)

