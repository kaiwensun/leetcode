# @param {Integer[]} candies
# @param {Integer} extra_candies
# @return {Boolean[]}
def kids_with_candies(candies, extra_candies)
    min = candies.max - extra_candies
    candies.map { |candy| candy >= min }
end
