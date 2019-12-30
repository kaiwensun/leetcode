# @param {Integer} n
# @return {Integer[]}
def sum_zero(n)
    half = n / 2
    (1..half).to_a + (-half..-1).to_a + (n.odd? ? [0] : [])
end
