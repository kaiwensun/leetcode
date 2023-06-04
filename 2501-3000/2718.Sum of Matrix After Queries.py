class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        cols_override, rows_override = set(), set()
        overrides = []
        for is_col, index, val in reversed(queries):
            if is_col:
                if index in cols_override:
                    overrides.append(0)
                else:
                    cols_override.add(index)
                    overrides.append(n - len(rows_override))
            else:
                if index in rows_override:
                    overrides.append(0)
                else:
                    rows_override.add(index)
                    overrides.append(n - len(cols_override))
        overrides.reverse()
        res = 0
        for i, query in enumerate(queries):
            res += query[2] * overrides[i]
        return res

