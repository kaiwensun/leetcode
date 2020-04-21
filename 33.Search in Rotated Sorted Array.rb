# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search(nums, target)
    lo, hi = 0, nums.size
    while lo < hi
        mid = (lo + hi) / 2
        if nums[0] <= target == nums[0] <= nums[mid]
            mid_num = nums[mid]
        else
            mid_num = nums[0] < nums[mid] ? -1.0/0.0 : 1.0/0.0
        end
        if target < mid_num
            hi = mid
        elsif target > mid_num
            lo = mid + 1
        else
            return mid
        end
    end
    -1
end
