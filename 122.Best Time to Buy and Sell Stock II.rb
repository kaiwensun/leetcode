# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    profit = 0
    (1...prices.size).each { |i| profit += [prices[i] - prices[i - 1], 0].max }
    profit
end
