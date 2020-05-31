# @param {String} s
# @param {Integer[][]} shift
# @return {String}
def string_shift(s, shift)
    sft = shift.reduce(0) { |acc, sft| acc + (sft[0].zero? ? sft[1] : -sft[1]) }
    sft %= s.size
    s[sft..-1] + s[0...sft]
end
