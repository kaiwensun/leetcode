# @param {String} s
# @return {Integer}
def first_uniq_char(s)
    cnt = Hash.new 0
    s.each_char { |c| cnt[c] += 1 }
    s.each_char.with_index { |c, index| return index if cnt[c] == 1 }
    -1
end
