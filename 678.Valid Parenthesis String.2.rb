# @param {String} s
# @return {Boolean}
def check_valid_string(s)
    lo = hi = 0
    s.each_char do | c |
        case c
            when "("
                lo += 1
                hi += 1
            when ")"
                lo -= 1
                hi -= 1
            when "*"
                hi += 1
                lo -= 1
        end
        if hi < 0
            return false
        end
        lo = [lo, 0].max
    end
    lo == 0
end
