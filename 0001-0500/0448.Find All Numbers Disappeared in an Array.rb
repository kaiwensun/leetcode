# @param {Integer[]} nums
# @return {Integer[]}
def find_disappeared_numbers(nums)
    mx = nums.max
    for num in nums
        nums[(num - 1) % mx] += mx
    end
    nums.each_with_index.select  { |num, i| num <= mx } .map { |_, index| index + 1 }
end

