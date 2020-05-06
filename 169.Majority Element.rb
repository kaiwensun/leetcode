# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    res = nil
    cnt = 0
    nums.each do |num|
        if res == num || cnt == 0
            res = num
            cnt += 1
        else
            cnt -= 1
        end
    end
    res
end
