from collections import namedtuple

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        Item = namedtuple('Item', ['lchar', 'lcnt', 'rchar', 'rcnt', 'maxcnt', 'full'])

        def sync_from_children(i):
            l = i * 2
            r = l + 1
            left = tree[l]
            right = tree[r]
            lchar = left.lchar
            rchar = right.rchar
            if left.full and left.lchar == right.lchar:
                lcnt = left.lcnt + right.lcnt
            else:
                lcnt = left.lcnt
            if right.full and right.rchar == left.rchar:
                rcnt = right.rcnt + left.rcnt
            else:
                rcnt = right.rcnt
            maxcnt = max(left.maxcnt, right.maxcnt)
            if left.rchar == right.lchar:
                maxcnt = max(maxcnt, left.rcnt + right.lcnt)
            tree[i] = Item(lchar, lcnt, rchar, rcnt, maxcnt, left.rchar == right.lchar and left.full and right.full)
            return maxcnt

        complete_len = len(s)
        for shift in [1, 2, 4, 8, 16]:
            complete_len |= complete_len >> shift
        complete_len += 1
        tree = [None] * complete_len + [Item(s[i], 1, s[i], 1, 1, True) for i in range(len(s))] + [Item(None, 0, None, 0, 0, True) for _ in range(complete_len - len(s))]

        for i in range(complete_len - 1, 0, -1):
            sync_from_children(i)
        res = []

        for c, i in zip(queryCharacters, queryIndices):
            leaf_index = i + complete_len
            if tree[leaf_index].lchar != c:
                tree[leaf_index] = Item(c, 1, c, 1, 1, True)
                index = leaf_index // 2
                while index:
                    sync_from_children(index)
                    index //= 2
            res.append(tree[1].maxcnt)
        return res

