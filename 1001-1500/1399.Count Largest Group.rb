# @param {Integer} n
# @return {Integer}
def count_largest_group(n)
    group = Hash.new 0
    (1..n).each { |x| group[x.to_s.split("").map(&:to_i).sum] += 1 }
    mx = group.values.max
    group.values.select { |value| value == mx }.size
end
