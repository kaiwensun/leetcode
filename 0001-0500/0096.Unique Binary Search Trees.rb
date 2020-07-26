# @param {Integer} n
# @return {Integer}
def num_trees(n)
    dp = Array.new(n + 1, 0)
    dp[0] = 1
    for treesize in (1..n)
        for lsize in (0..treesize - 1)
            rsize = treesize - lsize - 1
            dp[treesize] += dp[lsize] * dp[rsize]
        end
    end
    dp[-1]
end
