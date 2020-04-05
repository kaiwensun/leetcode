# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
    res = cur = 0
    mx = nums.max
    if mx < 0
        mx
    else
        nums.each do |n|
            cur = [cur + n, 0].max
            res = [res, cur].max
        end
        res
    end
end
