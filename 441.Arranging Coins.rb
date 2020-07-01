# @param {Integer} n
# @return {Integer}
def arrange_coins(n)
    # (1 + x) * x / 2 == n + d
    # x ^ 2 + x - (n + d) * 2 == 0
    # x = (-1 + sqrt(1 + 4*(n + d) * 2))/(2)
    (Math.sqrt(1 + 8 * n) - 1).to_i / 2
end
