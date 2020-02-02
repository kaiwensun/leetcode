import functools

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        @functools.lru_cache(None)
        def jump(index):
            res = 0
            for direction in [-1, 1]:
                for x in range(1, d + 1):
                    j = index + x * direction
                    if 0 <= j < len(arr) and arr[j] < arr[index]:
                        res = max(res, jump(j))
                    else:
                        break
            return res + 1
        return max(jump(index) for index in range(len(arr)))
