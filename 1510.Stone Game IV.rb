# @param {Integer} n
# @return {Boolean}
def winner_square_game(n)
    dp = Array.new(n + 1)
    dp[0] = false
    win(n, dp)
end

def win(n, dp)
    if dp[n].nil?
        dp[n] = false
        i = 1
        prev = n - i * i
        while prev >= 0
            dp[prev] = win(prev, dp)
            if !dp[prev]
                dp[n] = true
                break
            end
            i += 1
            prev = n - i * i
        end
    end
    dp[n]
end
