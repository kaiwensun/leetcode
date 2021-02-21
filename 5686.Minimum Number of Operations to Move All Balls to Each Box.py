class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        boxes = map(int, boxes)
        res = [0] * len(boxes)
        cnt = steps = 0
        for i in xrange(len(boxes)):
            res[i] = steps
            cnt += boxes[i]
            steps += cnt
        cnt = steps = 0
        for i in xrange(len(boxes) - 1, -1, -1):
            res[i] += steps
            cnt += boxes[i]
            steps += cnt
        return res


