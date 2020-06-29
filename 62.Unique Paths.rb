# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def unique_paths(m, n)
    dp = Array.new(n, 1)
    for _ in (1...m)
        for j in (1...n)
            dp[j] += dp[j - 1]
        end
    end
    dp[-1]
end
