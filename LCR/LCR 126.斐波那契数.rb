# @param {Integer} n
# @return {Integer}
MOD = 10 ** 9 + 7
def fib(n)
    a, b = 0, 1
    (n - 1).times do
        a, b = b, a + b
    end
    return n.zero? ? 0 : b % MOD
end

