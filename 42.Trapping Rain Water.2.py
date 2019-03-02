class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        rval = 0
        max_from_left_id = max_from_right_id = 0
        for i in xrange(len(height)):
            if height[max_from_left_id] < height[i]:
                max_from_left_id = i
            if height[max_from_left_id] == height[i]:
                max_from_right_id = i
        max_so_far = 0
        for i in xrange(max_from_left_id):
            rval += max(0, max_so_far - height[i])
            max_so_far = max(max_so_far, height[i])
        max_so_far = 0
        for i in xrange(len(height) - 1, max_from_right_id, - 1):
            rval += max(0, max_so_far - height[i])
            max_so_far = max(max_so_far, height[i])
        rval += (max_from_right_id - max_from_left_id) * (height[max_from_left_id] if height else 0)
        for i in xrange(max_from_left_id, max_from_right_id):
            rval -= height[i]
        return rval
