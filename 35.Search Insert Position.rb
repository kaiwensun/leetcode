# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search_insert(nums, target)
    lo, hi = 0, nums.size
    while lo < hi
        mid = (lo + hi) / 2
        if nums[mid] >= target
            hi = mid
        else
            lo = mid + 1
        end
    end
    lo
end
