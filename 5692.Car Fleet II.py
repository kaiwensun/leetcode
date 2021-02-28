class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        res = [None] * len(cars)
        history = [(float("inf"),) * 2]
        for i in xrange(len(cars) - 1, -1, -1):
            posi, speed = cars[i]
            if speed <= history[0][1]:
                res[i] = -1.0
                history = [(float("inf"), speed)]
            else:
                dist = cars[i + 1][0] - posi
                elapsed = 0
                while True:
                    last_elapsed, last_speed = history.pop()
                    if dist + last_elapsed * (last_speed - speed) <= 0:
                        remaining_time = last_elapsed - float(dist) / (speed - last_speed)
                        if remaining_time > 0.1 ** 6:
                            history.append((remaining_time, last_speed))
                        elapsed += float(dist) / (speed - last_speed)
                        history.append((elapsed, speed))
                        break
                    else:
                        dist += last_elapsed * (last_speed - speed)
                        elapsed += last_elapsed
                res[i] = elapsed
        return res

