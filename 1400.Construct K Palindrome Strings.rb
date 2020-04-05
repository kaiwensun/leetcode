# @param {String} s
# @param {Integer} k
# @return {Boolean}
def can_construct(s, k)
    counter = Hash.new 0
    s.each_char { |c| counter[c] ^= 1 }
    k <= s.size and counter.values.sum <= k
end
