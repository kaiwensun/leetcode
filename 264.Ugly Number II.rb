# @param {Integer} n
# @return {Integer}
def nth_ugly_number(n)
    pointers = [0, 0, 0]
    factors = [2,3,5].freeze
    buffer = [1]
    for _ in 1...n
        res = (0...3).map { |i| buffer[pointers[i]] * factors[i] }.min
        for i in 0...3
            pointers[i] += 1 if buffer[pointers[i]] * factors[i] == res
        end
        buffer << res
    end
    buffer[-1]
end
