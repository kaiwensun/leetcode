# @param {Integer} n
# @return {Boolean}

$dp = [false]
def winner_square_game(n)
    win(n)
end

def win(n)
    if $dp[n].nil?
        $dp[n] = false
        i = 1
        prev = n - i * i
        while prev >= 0
            $dp[prev] = win(prev)
            if !$dp[prev]
                $dp[n] = true
                break
            end
            i += 1
            prev = n - i * i
        end
    end
    $dp[n]
end
