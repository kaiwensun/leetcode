# @param {Integer[]} nums
# @return {Integer[]}
def largest_divisible_subset(nums)
    return nums if nums.empty?
    nums.sort!
    dp = Array.new(nums.size) { |_| [1, -1] }
    mx = mxidx = 0
    for i in 0...nums.size
        for j in i + 1 ... nums.size
            if nums[j] % nums[i] == 0 && dp[j][0] <= dp[i][0]
                dp[j] = [dp[i][0] + 1, i]
                if dp[j][0] > mx
                    mx, mxidx = dp[j][0], j
                end
            end
        end
    end
    collector = mxidx
    res = []
    while collector != -1
        res << nums[collector]
        collector = dp[collector][1]
    end
    res
end
