class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        # k %= n
        remain = n
        players = [True] * n
        i = 0
        
        def nextId(i):
            i %= n
            while not players[i]:
                i += 1
                i %= n
            return i

        for remain in range(n, 1, -1):
            for _ in range(k - 1):
                i = nextId(i + 1)
                # print(i)
            players[i] = False
            i = nextId(i + 1)
        return i + 1

