# @param {Integer[]} nums
# @return {Integer}
def longest_subarray(nums)
    return 0 if nums.size <= 1
    left = Array.new(nums)
    right = Array.new(nums)
    for i in (1...nums.size)
        left[i] = 1 + left[i - 1] if left[i] == 1
        right[nums.size - 1 - i] = 1 + right[nums.size - i] if right[nums.size - 1 - i] == 1
    end
    res = [left[-2], right[1]].max
    for i in (0 + 1...nums.size - 1)
        res = [res, left[i - 1] + right[i + 1]].max
    end
    return res
end
