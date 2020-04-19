# @param {Integer[]} nums
# @return {Integer}
def min_start_value(nums)
    res = 1.0/0.0
    nums.reduce(0) { |sum, n| res = [sum + n, res].min; sum + n }
    [-res + 1, 1].max
end
