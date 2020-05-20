class StockSpanner
    def initialize()
        @stack = [[1.0 / 0, -1]]
        @index = 0
    end


=begin
    :type price: Integer
    :rtype: Integer
=end
    def next(price)
        until @stack[-1][0] > price
            @stack.pop
        end
        @stack.push([price, @index])
        @index += 1
        @stack[-1][1] - @stack[-2][1]
    end


end

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner.new()
# param_1 = obj.next(price)
