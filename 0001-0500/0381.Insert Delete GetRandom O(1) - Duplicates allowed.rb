class RandomizedCollection

=begin
    Initialize your data structure here.
=end
    def initialize()
        @array = []
        @map = Hash.new { |h, k| h[k] = Set.new }
    end


=begin
    Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
    :type val: Integer
    :rtype: Boolean
=end
    def insert(val)
        put(val, @array.size)
        @map[val].size == 1
    end


=begin
    Removes a value from the collection. Returns true if the collection contained the specified element.
    :type val: Integer
    :rtype: Boolean
=end
    def remove(val)
        if @map[val].empty?
            false
        else
            index = @map[val].first
            del(index)
            if index != @array.size
                new_val = del(@array.size - 1)
                put(new_val, index)
            end
            true
        end
    end


=begin
    Get a random element from the collection.
    :rtype: Integer
=end
    def get_random()
        @array[rand(@array.size)]
    end

    private
    
    def put(val, index)
        @array[index] = val
        @map[val] << index
    end
    
    def del(index)
        val = @array[index]
        @array.pop if index == @array.size - 1
        @map[val].delete index
        val
    end

end

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection.new()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.get_random()
