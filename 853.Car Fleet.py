class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        posi_speed_list = sorted(zip(position, speed))
        time = res = 0
        for posi, speed in posi_speed_list[::-1]:
            ideal_time = (target - posi) / float(speed)
            if ideal_time > time:
                res += 1
                time = ideal_time
        return res
