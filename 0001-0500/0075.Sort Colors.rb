# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def sort_colors(nums)
    l, p, r = 0, 0, nums.size - 1
    while p <= r
        case nums[p]
        when 0
            nums[l], nums[p] = nums[p], nums[l]
            l += 1
            p = [l, p].max
        when 1
            p += 1
        when 2
            nums[r], nums[p] = nums[p], nums[r]
            r -= 1
        end
    end
end
