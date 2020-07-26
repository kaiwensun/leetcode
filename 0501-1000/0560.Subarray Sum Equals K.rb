# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_sum(nums, k)
    seen = Hash.new 0
    sum = res = 0
    seen[0] = 1
    nums.each do |num|
        sum += num
        res += seen[sum - k]
        seen[sum] += 1
    end
    res
end
