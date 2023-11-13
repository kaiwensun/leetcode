class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        MAX = 1 << 21 - 1

        Trie = lambda: defaultdict(Trie)
        trie = Trie()

        def add(num):
            mask = MAX
            p = trie
            while mask:
                p = p[mask & num]
                mask >>= 1
            p[True] = num

        def delete(p, mask, num):
            if mask == 0:
                del p[True]
                return p
            bit = mask & num
            if not delete(p[bit], mask >> 1, num):
                del p[bit]
            return p

        def get_partner(num):
            mask = MAX
            p = trie
            while mask:
                bit = num & mask
                if bit ^ mask in p:
                    p = p[bit ^ mask]
                else:
                    p = p[bit]
                mask >>= 1
            assert True in p
            return p[True]

        nums = list(set(nums))
        nums.sort()
        twice_i = 0
        res = 0
        for i, num in enumerate(nums):
            while twice_i < len(nums) and nums[twice_i] <= 2 * num:
                add(nums[twice_i])
                twice_i += 1
            res = max(res, num ^ get_partner(num))
            delete(trie, MAX, num)

        return res

