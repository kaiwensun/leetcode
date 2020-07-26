# @param {String} s
# @return {String}
require 'openssl'

RADIX = 26
MOD = 2 ** 63 - 1

def longest_dup_substring(s)
    array = s.each_char.map(&:ord)
    lo, hi = 0, s.size
    res = nil
    while lo < hi
        mid = (lo + hi) / 2
        test_res = test(mid, array)
        if test_res
            lo = mid + 1
            res = test_res
        else
            hi = mid
        end
    end
    res.nil? ? "" : s[(res - lo + 2)...(res + 1)]
end

def test(size, array)
    seen = Set.new
    top_radix = RADIX.to_bn.mod_exp(size - 1, MOD)
    hash = (0...size).to_a.inject(0) { |acc, i| (acc * RADIX + array[i]) % MOD }
    seen << hash
    for i in size...array.size
        hash = rolling_hash(size, i, array, hash, top_radix)
        if seen.include? hash
            return i
        end
        seen << hash
    end
    return nil
end

def rolling_hash(size, index, array, hash, top_radix)
    if index >= size
        hash -= array[index - size] * top_radix
        hash %= MOD
    end
    hash *= RADIX
    hash += array[index]
    hash %= MOD
end
