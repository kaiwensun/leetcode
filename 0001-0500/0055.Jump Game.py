"""
Basic idea:
	greedy search from end/right to start/left. find the right-most position that can jump to the destination, then set this right-most position as the new destination. if it can jump to the old destination from another more left position, it must also can jump from the "more left position" to the new destination (then from the new destination to the old destination). that is why greedy algorithm works

your runtime beats 85.81% of python submissions
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        posi = len(nums)-1
        for i in xrange(len(nums)-1,-2,-1):
            if i==-1:
                if posi==0:
                    return True
                else:
                    return False
            if posi-i<=nums[i]:
                posi=i

