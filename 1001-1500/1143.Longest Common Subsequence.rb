# @param {String} text1
# @param {String} text2
# @return {Integer}
def longest_common_subsequence(text1, text2)
    text1, text2 = text2, text1 if text1.size < text2.size
    dp = [0] * (text2.size + 1)
    dp[0] = 0
    for i in (0...text1.size)
        topleft, left = dp[0], 0
        for j in (0...text2.size)
            top = dp[j + 1]
            if text1[i] == text2[j]
                dp[j + 1] = [topleft + 1, left, top].max
            else
                dp[j + 1] = [left, top].max
            end
            topleft, left = top, dp[j + 1]
        end
    end
    dp[-1]
end
