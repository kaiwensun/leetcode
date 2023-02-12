# @param {Integer[]} banned
# @param {Integer} n
# @param {Integer} max_sum
# @return {Integer}
def max_count(banned, n, max_sum)
    banned = banned.to_set
    cnt = 0
    sum = 0
    for x in (1..n).reject{ |x| banned.include? x } do
        sum += x
        break if sum > max_sum
        cnt += 1
    end
    cnt
end

