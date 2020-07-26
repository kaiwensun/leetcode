class MinStack

=begin
    initialize your data structure here.
=end
    def initialize()
        @stack = []
    end


=begin
    :type x: Integer
    :rtype: Void
=end
    def push(x)
        mn = @stack.empty? ? x : [x, @stack[-1][-1]].min
        @stack << [x, mn]
    end


=begin
    :rtype: Void
=end
    def pop()
        @stack.pop[-1]
    end


=begin
    :rtype: Integer
=end
    def top()
        @stack[-1][0]
    end


=begin
    :rtype: Integer
=end
    def get_min()
        @stack[-1][-1]
    end


end

# Your MinStack object will be instantiated and called as such:
# obj = MinStack.new()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.get_min()
