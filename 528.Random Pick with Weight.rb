class Solution

=begin
    :type w: Integer[]
=end
    def initialize(w)
        @array = [*w.each_with_index]
        (1...@array.size).each { |i| @array[i][0] += @array[i - 1][0] }
    end


=begin
    :rtype: Integer
=end
    def pick_index()
        target = rand(@array[-1][0])
        @array.bsearch { |x, _| x > target }.last
    end


end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(w)
# param_1 = obj.pick_index()
