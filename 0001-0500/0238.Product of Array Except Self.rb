# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
    res = [1] * nums.size
    (1...nums.size).each { |i| res[i] = res[i - 1] * nums[i - 1] }
    right = nums[-1]
    (nums.size - 2).downto(0).each do |i|
        res[i] *= right
        right *= nums[i]
    end
    res
end
