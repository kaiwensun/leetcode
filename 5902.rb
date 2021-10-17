# @param {String} s
# @return {Boolean}
def are_numbers_ascending(s)
    s.split.select { |token| '0' <= token[0] && token[0] <= '9' }.reduce([true, -1]) { |acc, num| [acc[0] && (acc[1] < num.to_i), num.to_i] }[0]
end

