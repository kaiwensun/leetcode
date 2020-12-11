class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        def make_palindromic(new_lhalf, old_rhalf):
            if len(new_lhalf) > len(old_rhalf):
                return [int(new_lhalf + "".join(new_lhalf[:len(old_rhalf)][::-1]))]
            elif len(new_lhalf) == len(old_rhalf):
                return [int(new_lhalf + new_lhalf[::-1])]
            else:
                return [int(new_lhalf + old_rhalf[0] + new_lhalf[::-1]), int(new_lhalf + "9" + new_lhalf[::-1])]

        size = len(n)
        rsize = size // 2
        lsize = size - rsize
        lhalf = n[:lsize]
        rhalf = n[-rsize:] if rsize else ""
        candidates = [9]
        candidates.extend(make_palindromic(lhalf, rhalf))
        candidates.extend(make_palindromic(str(int(lhalf) - 1), rhalf))
        candidates.extend(make_palindromic(str(int(lhalf) + 1), rhalf))
        res = float("inf")
        nint = int(n)
        for candidate in sorted(candidates):
            if candidate != nint and abs(candidate - nint) < abs(res - nint):
                res = candidate
        return str(res)

