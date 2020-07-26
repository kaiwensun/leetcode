def generatePath(r, c):
    return 'D' * r + 'R' * c + '!' + 'L' * c + 'U' * r
dic = {}
board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
for r in xrange(len(board)):
    for c in xrange(len(board[r])):
        dic[board[r][c]] = (r, c)

class Solution(object):
    def alphabetBoardPath(self, target):
        def goto(r1, c1, r2, c2):
            r = abs(r2 - r1)
            c = abs(c2 - c1)
            r_letter = 'D' if r2 > r1 else 'U'
            c_letter = 'R' if c2 > c1 else 'L'
            if r2 == 5 and c2 == 0:
                return c_letter * c + r_letter * r + '!'
            return r_letter * r + c_letter * c + '!'
        res = []
        for src, dst in zip('a' + target[:-1], target):
            res.append(goto(dic[src][0], dic[src][1], dic[dst][0], dic[dst][1]))
        return ''.join(res)
