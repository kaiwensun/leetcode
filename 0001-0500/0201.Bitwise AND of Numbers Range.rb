# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def range_bitwise_and(m, n)
    res = num = m
    for i in (0...31) do
        next if (1 << i) & num == 0
        num += (1 << i)
        break if num > n
        res &= num
    end
    res
end
