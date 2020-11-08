MOD = 10 ** 9 + 7
class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        def sweep_right(binary):
            for sweep in (1, 2, 4, 8, 16):
                binary |= binary >> sweep
            return binary + 1

        mn = min(instructions)
        for i in xrange(len(instructions)):
            instructions[i] -= mn
        SIZE = max(instructions) + 1
        complete = sweep_right(SIZE)
        bit = [0] * (SIZE * 2)
        cost = 0
        for num in instructions:
            num += complete
            if num >= len(bit):
                num -= SIZE
            left = right = 0
            while num:
                bit[num] += 1
                if num & 1:
                    left += bit[num ^ 1]
                else:
                    right += bit[num ^ 1]
                num >>= 1
            cost += min(left, right)
            cost %= MOD
        return cost

