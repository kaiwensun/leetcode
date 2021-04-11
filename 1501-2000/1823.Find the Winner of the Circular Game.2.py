class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        tail = ListNode(n)
        p = tail
        for val in range(n - 1, 0, -1):
            p = ListNode(val, p)
        tail.nxt = p
        p = tail
        for _ in range(n):
            for __ in range(k - 1):
                p = p.nxt
            p.nxt = p.nxt.nxt
        return p.val

