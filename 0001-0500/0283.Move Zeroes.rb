# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
    l = r = 0
    (0...nums.size).each do |r|
        nums[r], nums[l] = 0, nums[r]
        l += nums[l] == 0 ? 0 : 1
    end
end
