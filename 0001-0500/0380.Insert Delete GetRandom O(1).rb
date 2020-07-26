class RandomizedSet

=begin
    Initialize your data structure here.
=end
    def initialize()
        @array = []
        @map = {}
    end


=begin
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    :type val: Integer
    :rtype: Boolean
=end
    def insert(val)
        if !@map.include? val
            @map[val] = @array.size
            @array << val
            true
        else
            false
        end
    end


=begin
    Removes a value from the set. Returns true if the set contained the specified element.
    :type val: Integer
    :rtype: Boolean
=end
    def remove(val)
        if @map.include? val
            index = @map.delete val
            @map[@array[-1]] = index if val != @array[-1]
            @array[index] = @array[-1]
            @array.pop
            true
        else
            false
        end
    end


=begin
    Get a random element from the set.
    :rtype: Integer
=end
    def get_random()
        @array[rand(@array.size)]
    end


end

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet.new()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.get_random()
