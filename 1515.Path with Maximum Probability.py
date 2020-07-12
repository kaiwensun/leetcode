import math
ACCURACY = 10 ** -5
class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        
        def getEuclideanDistSum(cx, cy):
            dist = 0.0
            for x, y in positions:
                dist += math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
            return dist
        x = y = 0
        step = 10
        dist_sum = getEuclideanDistSum(x, y)
        STEP_ACCURACY = ACCURACY / 10 / float(len(positions))
        while step > STEP_ACCURACY:
            directions = [[0, step], [0, -step], [step, 0], [-step, 0]]
            dist_sums = [getEuclideanDistSum(x + dx, y + dy) for dx, dy in directions]
            if min(dist_sums) < dist_sum:
                index = dist_sums.index(min(dist_sums))
                x += directions[index][0]
                y += directions[index][1]
                dist_sum = getEuclideanDistSum(x, y)
            else:
                step /= float(2)
        return dist_sum
