# @param {Integer} n
# @return {Boolean}
def is_power_of_two(n)
    !n.zero? && n - 1 & n == 0
end
