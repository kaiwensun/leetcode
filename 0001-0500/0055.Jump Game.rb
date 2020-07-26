# @param {Integer[]} nums
# @return {Boolean}
def can_jump(nums)
    mx = 0
    for i in (0...nums.size)
        break if i > mx
        mx = [mx, i + nums[i]].max
    end
    mx >= nums.size - 1
end
