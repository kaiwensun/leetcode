# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_distance(word1, word2)
    dp = (0..word2.size).to_a
    new_dp = Array.new(word2.size + 1)
    for i in 0...word1.size
        new_dp[0] = i + 1
        for j in 0...word2.size
            new_dp[j + 1] = [dp[j + 1] + 1,
                             new_dp[j] + 1,
                             dp[j] + (word1[i] == word2[j] ? 0 : 1)
                            ].min
        end
        dp, new_dp = new_dp, dp
    end
    dp[-1]
end
