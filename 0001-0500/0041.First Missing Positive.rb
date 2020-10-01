# @param {Integer[]} nums
# @return {Integer}
def first_missing_positive(nums)
    size = nums.size
    mod = size << 1
    for i in 0...nums.size
        if nums[i] <= 0 || nums[i] > size
            nums[i] = 0
        end
    end
    for i in 0...nums.size
        if !(nums[i] % mod).zero?
            nums[nums[i] % mod - 1] += mod
        end
    end
    for i in 0...nums.size
        if nums[i] < mod
            return i + 1
        end
    end
    size + 1
end

