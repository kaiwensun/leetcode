class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        res = 0
        for p in batteryPercentages:
            if p > res:
                res += 1
        return res

