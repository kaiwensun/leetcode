# @param {String} s
# @return {Integer}
def max_power(s)
    cnt = res = 0
    p = nil
    for c in s.each_char
        if c == p
            cnt += 1
        else
            p = c
            cnt = 1
        end
        res = [res, cnt].max
    end
    res
end
