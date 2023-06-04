# @param {Integer[]} nums
# @return {Integer}
def semi_ordered_permutation(nums)
    n = nums.size
    sum = nums.index(1) + n - 1 - nums.index(n)
    sum < n - 1 ? sum : sum - 1
end

