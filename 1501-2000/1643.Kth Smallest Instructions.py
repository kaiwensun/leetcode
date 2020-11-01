from math import comb

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        
        def search(row, col, k, res):
            if row == 0 or col == 0:
                res.append("H" * col + "V" * row)
                return
            hcount = comb(col - 1 + row, row)
            if k <= hcount:
                res.append("H")
                search(row, col - 1, k, res)
            else:
                res.append("V")
                search(row - 1, col, k - hcount, res)
        res = []
        search(destination[0], destination[1], k, res)
        return "".join(res)

