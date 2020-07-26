# @param {Integer[]} nums
# @return {Integer}
def find_max_length(nums)
    diff = 0
    diff2index = Hash.new (nums.size)
    diff2index[0] = -1
    res = 0
    for num, index in nums.each_with_index
        diff += num.zero? ? -1 : 1
        diff2index[diff] = [diff2index[diff], index].min
        res = [res, index - diff2index[diff]].max
    end
    res
end
