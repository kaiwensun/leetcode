# @param {Integer[]} nums
# @return {Integer}
def array_pair_sum(nums)
    nums.sort.values_at(*(0..nums.length - 1).step(2)).sum
end
