# @param {Integer} n
# @return {Integer[]}
def sum_zero(n)
    half = n / 2
    if n.odd?
        (1..half).to_a + (-half..-1).to_a + [0]
    else
        (1..half).to_a + (-half..-1).to_a
    end
end
