# @param {Integer} num
# @return {Integer}
def max_diff(num)
    s = num.to_s
    mx = s.gsub(s.chars.detect(->{"-"}) { |c| c != "9" }, "9")
    if s[0] == "1"
        mn = s.gsub(s.chars.detect(->{"-"}) { |c| c != "0" && c != "1" }, "0")
    else
        mn = s.gsub(s[0], "1")
    end
    mx.to_i - mn.to_i
end
