class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        type: int
        """
        self.cache = {}
        cleaner = re.compile("(.)\\1{2,}")
        def cleanUp(board):
            new_board = cleaner.sub('', board)
            while True:
                new_board = cleaner.sub('', board)
                if new_board == board:
                    break
                board = new_board
            return board

        def helper(board, hand):
            if not board:
                return sum(hand.values())
            hash_key = (board, tuple(sorted(hand.iteritems())))
            if hash_key in self.cache:
                return self.cache[hash_key]
            rval = -1
            i = 0
            while i < len(board):
                key = board[i]
                has = collections.Counter(board[i:i + 3])[key]
                if has == 2 and board[i + 1] != board[i]:
                    has = 1
                needs = 3 - has
                if needs <= hand[key]:
                    hand[key] -= needs
                    new_board = board[:i] + board[i + has:]
                    new_board = cleanUp(new_board)
                    rval = max(rval, helper(new_board, hand))
                    hand[key] += needs
                    i += has
                else:
                    i += 1
            self.cache[hash_key] = rval
            return rval
                        
        hand_counter = collections.Counter(hand)
        rval = helper(board, hand_counter)
        if rval == -1:
            return -1
        return len(hand) - rval

