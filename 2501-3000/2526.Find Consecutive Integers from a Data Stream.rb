class DataStream

=begin
    :type value: Integer
    :type k: Integer
=end
    def initialize(value, k)
        @value = value
        @k = k
        @acc_cnt = 0
    end


=begin
    :type num: Integer
    :rtype: Boolean
=end
    def consec(num)
        @acc_cnt = num == @value ? @acc_cnt + 1 : 0
        return @acc_cnt >= @k
    end


end

# Your DataStream object will be instantiated and called as such:
# obj = DataStream.new(value, k)
# param_1 = obj.consec(num)

