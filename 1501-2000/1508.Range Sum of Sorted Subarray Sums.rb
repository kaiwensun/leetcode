# @param {Integer[]} nums
# @param {Integer} n
# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def range_sum(nums, n, left, right)
    prefix_sum = [0]
    for num in nums
        prefix_sum << prefix_sum[-1] + num
    end
    arr = []
    for i in 0...nums.size
        for j in i + 1..nums.size
            arr << prefix_sum[j] - prefix_sum[i]
        end
    end
    arr.sort!
    arr[left - 1..right - 1].sum % (10 ** 9 + 7)
end
