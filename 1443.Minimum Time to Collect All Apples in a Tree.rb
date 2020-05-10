# @param {String[]} pizza
# @param {Integer} k
# @return {Integer}
MOD = 10 ** 9 + 7
def ways(pizza, k)
    m, n = pizza.size, pizza[0].size
    remainApples = Array.new(m) { Array.new(n, 0) }
    for i in (m - 1).downto(0)
        rightApple = 0
        for j in (n - 1).downto(0)
            rightApple += 1 if pizza[i][j] == "A"
            remainApples[i][j] += remainApples[i + 1][j] if i != m - 1
            remainApples[i][j] += rightApple
        end
    end
    dp = Array.new(m) { Array.new(n, 0) }
    last_dp = Array.new(m) { Array.new(n, 0) }
    for remainsPieces in (1..k)
        for j in (n - 1).downto(0)
            for i in (m - 1).downto(0)
                dp[i][j] = 0
                if remainsPieces == 1
                    dp[i][j] = 1 if remainApples[i][j] > 0
                elsif remainApples[i][j] >= remainsPieces
                    for new_i in (i + 1...m)
                        if remainApples[i][j] != remainApples[new_i][j]
                            dp[i][j] += last_dp[new_i][j]
                            dp[i][j] %= MOD
                        end
                    end
                    for new_j in (j + 1...n)
                        if remainApples[i][j] != remainApples[i][new_j]
                            dp[i][j] += last_dp[i][new_j]
                            dp[i][j] %= MOD
                        end
                    end
                end
            end
        end
        dp, last_dp = last_dp, dp
    end
    last_dp[0][0]
end
