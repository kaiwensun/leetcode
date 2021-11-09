from functools import cache
from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
        cnt = Counter(hand)
        remain_hand = tuple(cnt[c] for c in "RYBGW")
        board = tuple("RYBGW".index(c) for c in board)

        def clean(board, i):
            if not 0 <= i < len(board):
                return board
            l = r = i
            while l >=0 and board[l] == board[i]:
                l -= 1
            while r < len(board) and board[r] == board[i]:
                r += 1
            if r - l > 3:
                board = board[:l + 1] + board[r:]
                return clean(board, l)
            return board

        @cache
        def dfs(board, remain_hand):
            if not board:
                return sum(remain_hand)
            res = float("-inf")
            remain_hand = list(remain_hand)
            for j in range(len(remain_hand)):
                if remain_hand[j] == 0:
                    continue
                for i in range(len(board) + 1):
                    remain_hand[j] -= 1
                    res = max(res, dfs(clean(board[:i] + (j,) + board[i:], i), tuple(remain_hand)))
                    remain_hand[j] += 1
            return res

        res = dfs(board, remain_hand)
        return sum(remain_hand) - res if res != float("-inf") else -1

