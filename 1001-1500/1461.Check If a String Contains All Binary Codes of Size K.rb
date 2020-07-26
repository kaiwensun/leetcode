# @param {String} s
# @param {Integer} k
# @return {Boolean}
def has_all_codes(s, k)
    set = Set.new
    mask = (1 << k) - 1
    base = s[0...(k - 1)].to_i
    for i in (k - 1)...s.size
        base = ((base << 1) | s[i].to_i) & mask
        set << base
    end
    set.size == 2 ** k
end
