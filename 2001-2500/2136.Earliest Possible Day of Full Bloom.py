class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        res = cur = 0
        for grow, plant in sorted(zip(growTime, plantTime), reverse=True):
            cur += plant
            res = max(res, cur + grow)
        return res

