# @param {Integer} n
# @return {String[]}
def simplified_fractions(n)
    res = []
    for num in (1...n)
        for den in (num + 1 .. n)
            res << "#{num}/#{den}" if num.gcd(den) == 1
        end
    end
    res
end
