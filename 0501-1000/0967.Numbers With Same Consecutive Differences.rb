# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def nums_same_consec_diff(n, k)
    if n == 1
        return (0..9).to_a
    else
        acc = []
        (1..9).each { |num| dfs(n, k, num, acc) }
        return acc
    end
end

def dfs(n, k, num, acc)
    if n == 1
        acc << num
    else
        dfs(n - 1, k, num * 10 + (num % 10) - k, acc) if (num % 10 - k >= 0)
        dfs(n - 1, k, num * 10 + (num % 10) + k, acc) if (num % 10 + k <= 9) && k != 0
    end
end
