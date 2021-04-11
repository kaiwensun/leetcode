import collections
import heapq

class MKAverage:

    def __init__(self, m: int, k: int):
        
        self.i = 0
        self.m = m
        self.k = k
        self.queue = collections.deque()
        self.index2position = {}  # -1: ksmallest; 0: mid; +1: klargest
        
        self.ksmallest = []
        self.ksmallest_sum = 0
        self.ksmallest_size = 0
        
        self.klargest = []
        self.klargest_sum = 0
        self.klargest_size = 0

        self.mid_min_heap = []
        self.mid_max_heap = []
        self.mid_sum = 0
        self.mid_size = 0
        
    def addElement(self, num: int) -> None:
        self._expire_queue_head()
        self._prune_heaps()

        self.queue.append(num)
        heapq.heappush(self.mid_min_heap, (num, self.i))
        heapq.heappush(self.mid_max_heap, (-num, self.i))
        self.index2position[self.i] = 0
        self.mid_sum += num
        self.mid_size += 1
        self._prune_heaps()
            
        if self.ksmallest_size == self.k and self.mid_size > 0 and -self.ksmallest[0][0] > self.mid_min_heap[0][0]:
            # swap ksmallest and mid

            s = self.ksmallest[0]
            m = self.mid_min_heap[0]
            heapq.heapreplace(self.ksmallest, (-m[0], m[1]))
            heapq.heapreplace(self.mid_min_heap, (-s[0], s[1]))

            self.index2position[m[1]] = -1
            self.index2position[s[1]] = 0

            self._prune_heaps()

            heapq.heappush(self.mid_max_heap, s)

            self.ksmallest_sum += s[0] + m[0]
            self.mid_sum -= s[0] + m[0]

            self._prune_heaps()
            
        if self.ksmallest_size < self.k:
            # move mid to smallest

            m = self.mid_min_heap[0]
            heapq.heappush(self.ksmallest, (-m[0], m[1]))
            self.ksmallest_sum += m[0]
            self.ksmallest_size += 1

            self.index2position[m[1]] = -1
            self._prune_heaps()
            self.mid_sum -= m[0]
            self.mid_size -= 1
            
        
        if self.klargest_size == self.k and self.mid_size > 0 and self.klargest[0][0] < -self.mid_max_heap[0][0]:
            # swap klargest and mid
            l = self.klargest[0]
            m = self.mid_max_heap[0]
            heapq.heapreplace(self.klargest, (-m[0], m[1]))
            heapq.heapreplace(self.mid_max_heap, (-l[0], l[1]))
            
            self.index2position[m[1]] = 1
            self.index2position[l[1]] = 0
            
            self._prune_heaps()
            
            heapq.heappush(self.mid_min_heap, l)
            
            self.klargest_sum -= l[0] + m[0]
            self.mid_sum += l[0] + m[0]
            
            self._prune_heaps()
            
        if self.klargest_size < self.k and self.mid_size > 0:
            # move mid to largest
            
            m = self.mid_max_heap[0]
            heapq.heappush(self.klargest, (-m[0], m[1]))
            self.klargest_sum -= m[0]
            self.klargest_size += 1
            
            self.index2position[m[1]] = 1
            self._prune_heaps()
            self.mid_sum += m[0]
            self.mid_size -= 1

        self.i += 1
        
    def _expire_queue_head(self):
        exp_index = self.i - self.m
        if exp_index < 0:
            return
        posi = self.index2position[exp_index]
        head = self.queue.popleft()
        if posi == -1:
            self.ksmallest_sum -= head
            self.ksmallest_size -= 1
        elif posi == 0:
            self.mid_sum -= head
            self.mid_size -= 1
        else:
            self.klargest_sum -= head
            self.klargest_size -= 1
        del self.index2position[exp_index]


    def _prune_heaps(self):
        exp_index = self.i - self.m
        for heap, posi in zip((self.ksmallest, self.mid_min_heap, self.mid_max_heap, self.klargest), (-1, 0, 0, 1)):
            while heap and (heap[0][1] <= exp_index or self.index2position[heap[0][1]] != posi):
                heapq.heappop(heap)

    def calculateMKAverage(self) -> int:
        if self.i < self.m:
            return -1
        return self.mid_sum // (self.m - self.k * 2)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

