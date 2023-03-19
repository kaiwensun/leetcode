# @param {Integer[]} nums
# @param {Integer} value
# @return {Integer}
def find_smallest_integer(nums, value)
    cnt = Hash.new { |h, k| h[k] = 0 }
    nums.each_with_index do |num, i|
        num %= value
        nums[i] = cnt[num] * value + num
        cnt[num] += 1
    end
    nums.sort!
    for num, i in nums.each_with_index do
        if i != num
            return i
        end
    end
    return nums.size
end

