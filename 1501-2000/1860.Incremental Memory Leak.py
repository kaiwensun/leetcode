class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        memories = [memory1, memory2]
        t = 1
        while True:
            i = 0 if memories[0] >= memories[1] else 1
            if memories[i] - t < 0:
                break
            memories[i] -= t
            t += 1
        return [t] + memories

