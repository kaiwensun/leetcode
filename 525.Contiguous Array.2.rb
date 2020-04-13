# @param {Integer[]} nums
# @return {Integer}
def find_max_length(nums)
    seen = {}
    seen[0] = -1
    res = cnt = 0
    nums.each_with_index do |x, index|
        cnt += x.zero? ? 1 : -1
        if seen.key? cnt
            res = [res, index - seen[cnt]].max
        else
            seen[cnt] = index
        end
    end
    res
end
