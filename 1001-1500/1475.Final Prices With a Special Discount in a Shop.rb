# @param {Integer[]} prices
# @return {Integer[]}
def final_prices(prices)
    stack = [0]
    res = []
    for price in prices.reverse
        stack.pop while stack[-1] > price
        res << [price - stack.last, 0].max
        stack << price if price != stack.last
    end
    res.reverse
end
