class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        queries = [q[0] ^ q[1] for q in queries]
        str_2_index = [[]]
        for length in range(1, 33):
            mapping = {}
            str_2_index.append(mapping)
            for i in range(len(s) - length + 1):
                mapping.setdefault(s[i: i + length], i)
        res = []
        for q in queries:
            q = bin(q)[2:]
            l = str_2_index[len(q)].get(q, -1)
            r = l + len(q) - 1 if l != -1 else -1
            res.append([l, r])
        return res

