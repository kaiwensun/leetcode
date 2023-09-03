class Solution:
    def minimumOperations(self, num: str) -> int:
        def find(d1, d2):
            res = 0
            found_d2 = False
            for c in reversed(num):
                if not found_d2 and c in d2:
                    found_d2 = True
                elif found_d2 and c in d1:
                    return res
                else:
                    res += 1
            return len(num) - 1 if '0' in num else len(num)
        return min(find({'0', '5'}, {'0'}), find({'2', '7'}, {'5'}))

