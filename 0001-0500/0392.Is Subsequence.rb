# @param {String} s
# @param {String} t
# @return {Boolean}
def is_subsequence(s, t)
    sp = 0
    for c in t.each_char
        sp += 1 if s[sp] == c
        break if sp == s.size
    end
    sp == s.size
end
