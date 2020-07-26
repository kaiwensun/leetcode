# @param {String} s
# @return {String}
def frequency_sort(s)
    cnt = Hash.new 0
    s.chars { |c| cnt[c] += 1 }
    cnt.sort_by { |k, v| -v } .map { |c, n| c * n}.join
end
