import functools
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        
        """
        j is as in seats[i][j].
        convert j to the corresponding binary mask of the row
        """
        def j2binary(j):
            return 1 << (n - j - 1)
        
        
        """
        Count number of 1 in the row
        """
        def count1(binary):
            res = 0
            while binary:
                binary &= (binary - 1)
                res += 1
            return res
        
        """
        Given the previousRow's seat settings, this DFS function generates all valid studnet placements for the i-th row.
        @prevRowBinary: studnet placement of previous row
        @i: i-th row
        @j: during the dfs, try not to place a student at the j-th seat of the row, then if valid try to place a student at the j-th seat
        @binary: the current placement for the first (j-1) seats of the row
        """
        def genNextRowBinary(prevRowBinary, i, j, binary):
            if j >= n:
                yield binary
            else:
                for res in genNextRowBinary(prevRowBinary, i, j + 1, binary):
                    yield res
                lMask = j2binary(j - 1)
                rMask = j2binary(j + 1) if j + 1 < n else 0
                if (prevRowBinary & lMask) | (binary & lMask) | (prevRowBinary & rMask) == 0 and seats[i][j] != "#":
                    binary |= j2binary(j)
                    for res in genNextRowBinary(prevRowBinary, i, j + 1, binary):
                        yield res

        """
        Given the i-th row is placed as binary, return the max num of students for the i-th row and rows after
        """
        @functools.lru_cache(None)
        def dp(i, binary):
            res = count1(binary)
            if i != m - 1:
                res += max(dp(i + 1, nextRowBinary) for nextRowBinary in genNextRowBinary(binary, i + 1, 0, 0))
            return res
        
        return max(dp(0, firstRowBinary) for firstRowBinary in genNextRowBinary(0, 0, 0, 0))
            
