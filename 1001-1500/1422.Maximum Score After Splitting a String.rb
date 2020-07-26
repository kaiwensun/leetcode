# @param {String} s
# @return {Integer}
def max_score(s)
    left = 0
    right = s.count("1")
    res = 0
    for (c, i) in s.chars.each_with_index
        if c == "0"
            left += 1
        else
            right -= 1
        end
        res = [res, left + right].max if i != s.size - 1
    end
    res
end
