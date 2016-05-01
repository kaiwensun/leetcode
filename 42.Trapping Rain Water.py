"""
Basic idea:
	there must be (one of) the highest bar that avoids all left-side water from flowing rightward, and avoids all right-side water from flowing leftward.
	On the left side of the highest bar, the water surface level is non-descending. On the right side of the highest bar, the water surface level is non-asceding.
	This solution finds the maximum bar at first. However, we don't have to do so. We can just scan from left to middle and scan from right to middle at the same time (lower bar of the two has priority). When the two scanner meets in the middle, we are done.
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height==[]:
            return 0
        peak = max(height)
        peak_ind = height.index(peak)
        volum = 0
        cur_highest=0
        for l in xrange(0,peak_ind):
            if height[l]>cur_highest:
                cur_highest=height[l]
            else:
                volum = volum+cur_highest-height[l]
        cur_highest=0
        for r in xrange(len(height)-1,peak_ind,-1):
            if height[r]>cur_highest:
                cur_highest = height[r]
            else:
                volum = volum+cur_highest-height[r]
        return volum
            

