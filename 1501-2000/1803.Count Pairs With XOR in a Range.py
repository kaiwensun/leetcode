class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:

        def dfs(num, p, prefix, mask):
            if mask == 0:
                return p["#"] if low <= prefix <= high else 0
            mn = prefix
            mx = prefix | ((mask << 1) - 1)
            if mn > high or mx < low:
                return 0
            if low <= mn and mx <= high:
                return p["#"]
            bit = num & mask
            res = 0
            for key in 0, mask:
                if key not in p:
                    continue
                xor = key ^ bit
                res += dfs(num, p[key], prefix | xor, mask >> 1)
            return res

        bit_size = len(bin(max(nums))) - 2
        Trie = lambda : defaultdict(Trie)
        trie = Trie()
        trie["#"] = 0
        res = 0
        for num in nums:
            mask = 1 << (bit_size - 1)
            res += dfs(num, trie, 0, mask)
            p = trie
            while mask:
                bit = num & mask
                p = p[bit]
                p.setdefault("#", 0)
                p["#"] += 1
                mask >>= 1
            trie["#"] += 1

        return res

