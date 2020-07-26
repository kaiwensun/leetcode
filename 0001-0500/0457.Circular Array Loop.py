class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        MAX = 10000
        def get_original_value(v):
            if is_visiting(v):
                return v - MAX
            if is_visited(v):
                return v - 2 * MAX
            return v
        def not_visited(v):
            return -1000 <= v <= 1000
        def is_visiting(v):
            return MAX - 1000 <= v <= MAX + 1000
        def is_visited(v):
            return 2 * MAX - 1000 <= v <= 2 * MAX + 1000
        def mark_visiting(v):
            return v + MAX
        def mark_visited_since(i):
            while is_visiting(nums[i]):
                nums[i] += MAX
                i = (i + nums[i] - 2 * MAX) % len(nums)
        
        for i in xrange(len(nums)):
            if is_visited(nums[i]):
                continue
            is_posi = nums[i] > 0
            j = i
            prevInd = -1
            while (get_original_value(nums[j]) > 0) is is_posi:
                v = nums[j]
                if is_visiting(v) and j != prevInd:
                    return True
                elif is_visited(v) or prevInd == j:
                    break
                else:
                    nums[j] = mark_visiting(nums[j])
                    prevInd = j
                    j = (nums[j] - MAX + j) % len(nums)
            mark_visited_since(i)
        return False
