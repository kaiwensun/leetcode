class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def canArrive(speed):
            time = 0
            for d in dist:
                time = math.ceil(time)
                time += d / speed
                if time > hour:
                    return False
            return True
            
        l, r = 1, 10 ** 7 + 1
        while l < r:
            mid = (l + r) // 2
            if canArrive(mid):
                r = mid
            else:
                l = mid + 1
        return -1 if l > 10 ** 7 else l
