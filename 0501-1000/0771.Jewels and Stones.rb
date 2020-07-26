# @param {String} j
# @param {String} s
# @return {Integer}
def num_jewels_in_stones(j, s)
    res = 0
    j = Set.new(j.chars)
    s.each_char { |c| res += (j.include?(c) ? 1 : 0) }
    res
end
