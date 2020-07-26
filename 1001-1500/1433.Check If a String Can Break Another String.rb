# @param {String} s1
# @param {String} s2
# @return {Boolean}
def check_if_can_break(s1, s2)
    s1 = s1.chars.sort.join
    s2 = s2.chars.sort.join
    s1, s2 = s2, s1 if s1 > s2
    s1.chars.zip(s2.chars).all? { |c1, c2| c1 <= c2 }
end
